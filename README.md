# Large-scale graph transformer

GROVER is a self-supervised Graph Neural Network for molecular representation pretrained with 10 million unlabelled molecules from ChEMBL and ZINC15. The model provided has been pre-trained on 10 million molecules (GROVERlarge). GROVER has then been fine-tuned to predict several activities from the MoleculeNet benchmark, consistently outperforming other state-of-the-art methods for serveral benchmark datasets.

This model was incorporated on 2021-07-02.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7w6n`
- **Slug:** `grover-embedding`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
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
| dim_0000 | float |  | Dimension 0 of the GROVER embedding |
| dim_0001 | float |  | Dimension 1 of the GROVER embedding |
| dim_0002 | float |  | Dimension 2 of the GROVER embedding |
| dim_0003 | float |  | Dimension 3 of the GROVER embedding |
| dim_0004 | float |  | Dimension 4 of the GROVER embedding |
| dim_0005 | float |  | Dimension 5 of the GROVER embedding |
| dim_0006 | float |  | Dimension 6 of the GROVER embedding |
| dim_0007 | float |  | Dimension 7 of the GROVER embedding |
| dim_0008 | float |  | Dimension 8 of the GROVER embedding |
| dim_0009 | float |  | Dimension 9 of the GROVER embedding |

_10 of 5000 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7w6n](https://hub.docker.com/r/ersiliaos/eos7w6n)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7w6n.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7w6n.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/tencent-ailab/grover](https://github.com/tencent-ailab/grover)
- **Publication**: [https://papers.nips.cc/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf](https://papers.nips.cc/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf)
- **Publication Type:** `Peer reviewed`
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
