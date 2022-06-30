# Large-scale graph transformer

## Model Identifiers
- Slug: grover-embedding
- Ersilia ID: eos7w6n
- Tags: fingerprint, ML, graph

## Model Description
Self-supervised graph transformer trained on large-scale small molecule data 
- Input: SMILES 
- Output: Vector 
- Model type: Regression
- Mode of training: Pretrained
- Training data: 11,000,000 compounds (https://github.com/tencent-ailab/grover/blob/main/grover/data/groverdataset.py)
- Experimentally validated: No 

## Source code
This model is published by Yu Rong et al Self-Supervised Graph Transformer on Large-Scale Molecular Data. *Curran Associates, Inc.* (2020). DOI: https://proceedings.neurips.cc/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf
- Code: https://github.com/tencent-ailab/grover
- Checkpoints: https://github.com/tencent-ailab/grover

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "grover", located at `/model` and licensed under a MIT License

## History 
- Model was downloaded and incorporated on September 21, 2021
