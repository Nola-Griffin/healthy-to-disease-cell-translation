# healthy-to-disease-cell-translation
A machine learning project exploring whether healthy single-cell transcriptomes can be transformed into disease-like transcriptomes. 
goals: 
- Learn PyTorch
- Learn Single-cell genomics
- Learn agentic AI workflows
- Build a reproducible research lab notebook

# Dataset

This project uses a single-cell RNA sequencing dataset obtained from CELLxGENE.

The dataset is not included in this repository because it exceeds GitHub's file size limits.

## Download

## Dataset

This project uses a publicly available single-cell RNA sequencing dataset from CELLxGENE.

Dataset title:

"Epithelial and immune cells - Bronchoalveolar lavage from paediatric cystic fibrosis (CF) and non-CF control participants"

Dataset characteristics:

- Organism: Homo sapiens
- Tissue: Lung
- Assay: 10x Genomics 3' v3
- Conditions: Cystic fibrosis and healthy controls
- Total cells: 13,687

The dataset is not included in this repository because it exceeds GitHub file size limits.

After downloading, save the file as:

data/cystic_fibrosis_investigation.h5ad

Create the following directory structure:

healthy-to-disease-cell-translation/
│
├── data/
│   └── cystic_fibrosis_investigation.h5ad
├── notebooks/
├── src/
└── README.md