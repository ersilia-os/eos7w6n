python grover/scripts/save_features.py --data_path data.csv \
                                       --save_path features.npz \
                                       --features_generator rdkit_2d_normalized \
                                       --restart

python grover/main.py fingerprint --data_path data.csv \
                                  --features_path features.npz \
                                  --checkpoint_path ../checkpoints/grover_large.pt \
                                  --fingerprint_source both \
                                  --output fp.npz \
                                  --no_cuda \
