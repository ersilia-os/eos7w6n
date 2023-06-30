# Large-scale graph transformer

GROVER is a self-supervised Graph Neural Network for molecular representation pretrained with 10 million unlabelled molecules from ChEMBL and ZINC15. The model provided has been pre-trained on 10 million molecules (GROVERlarge). GROVER has then been fine-tuned to predict several activities from the MoleculeNet benchmark, consistently outperforming other state-of-the-art methods for serveral benchmark datasets.

## Identifiers

* EOS model ID: `eos7w6n`
* Slug: `grover-embedding`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Embedding representation of a molecule

## References

* [Publication](https://papers.nips.cc/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf)
* [Source Code](https://github.com/tencent-ailab/grover)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos7w6n)

## Citation

If you use this model, please cite the [original authors](https://papers.nips.cc/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!