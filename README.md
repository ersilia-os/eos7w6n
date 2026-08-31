# Large-scale graph transformer

GROVER is a self-supervised Graph Neural Network for molecular representation pretrained with 10 million unlabelled molecules from ChEMBL and ZINC15. The model provided has been pre-trained on 10 million molecules (GROVERlarge). GROVER has then been fine-tuned to predict several activities from the MoleculeNet benchmark, consistently outperforming other state-of-the-art methods for serveral benchmark datasets.

This model was incorporated on 2021-09-22.Last packaged on 2026-04-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7w6n`
- **Slug:** `grover-embedding`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Chemical graph model`, `Embedding`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `5000`
- **Output Consistency:** `Fixed`
- **Interpretation:** Embedding representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_0000 | float |  | Feature 0 of the GROVER embedding |
| feat_0001 | float |  | Feature 1 of the GROVER embedding |
| feat_0002 | float |  | Feature 2 of the GROVER embedding |
| feat_0003 | float |  | Feature 3 of the GROVER embedding |
| feat_0004 | float |  | Feature 4 of the GROVER embedding |
| feat_0005 | float |  | Feature 5 of the GROVER embedding |
| feat_0006 | float |  | Feature 6 of the GROVER embedding |
| feat_0007 | float |  | Feature 7 of the GROVER embedding |
| feat_0008 | float |  | Feature 8 of the GROVER embedding |
| feat_0009 | float |  | Feature 9 of the GROVER embedding |

_10 of 5000 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7w6n](https://hub.docker.com/r/ersiliaos/eos7w6n)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7w6n.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7w6n.zip)

### Resource Consumption
- **Model Size (Mb):** `428`
- **Environment Size (Mb):** `2407`
- **Image Size (Mb):** `3695.78`

**Computational Performance (seconds):**
- 10 inputs: `31.93`
- 100 inputs: `69.45`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/tencent-ailab/grover](https://github.com/tencent-ailab/grover)
- **Publication**: [https://doi.org/10.48550/arXiv.2007.02835](https://doi.org/10.48550/arXiv.2007.02835)
- **Publication Type:** `Preprint`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7w6n
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7w6n
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
