import csv
import random

import numpy as np
import torch
import os
from rdkit import RDLogger

from grover.util.parsing import parse_args, get_newest_train_args
from grover.util.utils import create_logger
from task.cross_validate import cross_validate
from task.fingerprint import generate_fingerprints
from task.predict import make_predictions, write_prediction
from task.pretrain import pretrain_model
from grover.data.torchvocab import MolVocab

NBITS=5000

def setup(seed):
    # frozen random seed
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


if __name__ == '__main__':
    # setup random seed
    setup(seed=42)
    # Avoid the pylint warning.
    a = MolVocab
    # supress rdkit logger
    lg = RDLogger.logger()
    lg.setLevel(RDLogger.CRITICAL)

    # Initialize MolVocab
    mol_vocab = MolVocab

    # Ersilia calls: python main.py <input.csv> <output.csv>
    # GROVER expects: python main.py fingerprint --data_path <input.csv> --output_path <output.csv> --checkpoint_path <model.pt>
    import sys as _sys
    if len(_sys.argv) == 3 and not _sys.argv[1].startswith('--') and _sys.argv[1] not in ('finetune', 'eval', 'predict', 'fingerprint', 'pretrain'):
        root = os.path.dirname(os.path.abspath(__file__))
        checkpoint_path = os.path.join(root, '..', '..', 'checkpoints', 'grover_large.pt')
        input_path = _sys.argv[1]
        output_path = _sys.argv[2]
        features_path = input_path.replace('.csv', '_features.npz')
        # Generate RDKit 2D normalized features (200 dims appended to 4800 GROVER dims = 5000 total)
        from argparse import Namespace as _Namespace
        from scripts.save_features import generate_and_save_features as _gen_features
        _feats_args = _Namespace(
            data_path=input_path,
            features_generator='rdkit_2d_normalized',
            save_path=features_path,
            save_frequency=10000,
            restart=True,
            max_data_size=None,
            sequential=False,
        )
        _gen_features(_feats_args)
        _sys.argv = [_sys.argv[0], 'fingerprint',
                     '--data_path', input_path,
                     '--features_path', features_path,
                     '--output_path', output_path,
                     '--checkpoint_path', checkpoint_path,
                     '--fingerprint_source', 'both',
                     '--no_cuda']

    args = parse_args()
    if args.parser_name == 'finetune':
        logger = create_logger(name='train', save_dir=args.save_dir, quiet=False)
        cross_validate(args, logger)
    elif args.parser_name == 'pretrain':
        logger = create_logger(name='pretrain', save_dir=args.save_dir)
        pretrain_model(args, logger)
    elif args.parser_name == "eval":
        logger = create_logger(name='eval', save_dir=args.save_dir, quiet=False)
        cross_validate(args, logger)
    elif args.parser_name == 'fingerprint':
        train_args = get_newest_train_args()
        logger = create_logger(name='fingerprint', save_dir=None, quiet=False)
        feas = generate_fingerprints(args, logger)
        pred_file = args.output_path.replace('.csv', '.npz')
        np.savez_compressed(pred_file, fps=feas)
        V = np.load(pred_file)["fps"]
        header = ["dim_{0}".format(str(i).zfill(4)) for i in range(NBITS)]
        # write output in a .csv file
        with open(args.output_path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(header)  # header
            for i in range(V.shape[0]):
                writer.writerow(list(V[i,:]))
        if os.path.exists(pred_file):
            os.remove(pred_file)
    elif args.parser_name == 'predict':
        train_args = get_newest_train_args()
        avg_preds, test_smiles = make_predictions(args, train_args)
        write_prediction(avg_preds, test_smiles, args)
