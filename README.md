# ProtLoc-Mex1

## Introduction ProtLoc-Mex1

This project offers a comprehensive pipeline for the rapid development of subcellular localization prediction and model interpretation. It encompasses 42 amino acid feature characterization algorithms and Gene Ontology (GO) feature extraction based on the Doc2Vec approach. Additionally, two random forest models for protein localization prediction are provided. 

with support by SHAP package warped into ProtLoc-mex1 module，everyone can easily use two random forest models above to get the global explanation and local explanation of the feature (physiochemical characteristics of amino acid sequence and GO annotation semantics)  and model in  protein localization prediction.

## Installation 

This project's core code has been uploaded to the PyPI repository([protloc-mex1 · PyPI](https://pypi.org/project/protloc-mex1/)). To get it using a conda virtual environment, follow the steps below:

First, create a new conda environment (you can modify the environment name as needed, here we use "myenv" as an example):

```
conda create -n myenv python=3.10
```

Then, activate the environment you just created:

```
conda activate myenv
```

Finally, use pip to install 'protloc_mex1' within this environment:

```
pip install protloc_mex1
```

### Dependencies

ProtLoc-Mex1 requires Python  == 3.9 or 3.10.

Below are the Python packages required by ProtLoc-Mex1, which are automatically installed with it:

```
dependencies = [
        "biopython==1.79",
        "numpy==1.24.1",
        "pandas==1.4.1",
        "seaborn==0.11.2",
        "matplotlib==3.5.1",
        "shap==0.41.0",
        "gensim==4.2.0"
]
```

 and other not automatically installed but also required Python packages：

```
dependencies = [
       "scikit-learn>=1.0.2",
       "captum == 0.6.0"
       "torch == 1.12.1"
]
```

It is advised to obtain these dependent packages from their respective official sources, while carefully considering the implications of version compatibility.

## How to use ProtLoc-Mex1

ProtLoc-Mex1 includes 6 modules: AA_count, GO_count, classifier_evalute, SHAP_conduct,  SHAP_plus.

###  AA_count

In this module, we can perform protein sequence analysis. AA_count include three functions, `dna_sequence_conduct()`, `rna_sequence_conduct()`, and `protein_sequence_conduct()`, they are designed to process DNA, RNA, and protein sequences, respectively, in a given DataFrame `df`.

The `dna_sequence_conduct()` and `rna_sequence_conduct()` functions:

\1. Filter out illegal bases in the DNA/RNA sequences in the DataFrame.
\2. Calculate and add columns for the frequency of carbon, hydrogen, nitrogen, and oxygen elements in the DNA/RNA sequences.
\3. Calculate and add columns for the frequency of each base (A, T, C, G for DNA and A, U, C, G for RNA) in the DNA/RNA sequences.

The `protein_sequence_conduct()` function:

\1. Adds new columns for 20 standard amino acids, elemental properties, and various protein properties including molecular weight, aromaticity, instability index, flexibility, isoelectric point, secondary structure fraction, molar extinction coefficient for reduced cysteines and disulfide bridges, and gravy.
\2. Calculates and adds the frequency of each amino acid in the protein sequences.
\3. For sequences containing only 20 standard amino acids, it calculates and adds values for molecular weight, aromaticity, instability index, flexibility, isoelectric point, secondary structure fraction, molar extinction coefficient for reduced cysteines and disulfide bridges, and gravy.
\4. Calculates and adds the count of each element (oxygen, sulfur, carbon, hydrogen, nitrogen) and acidic, basic, polar, and non-polar properties in the protein sequences.

for using AA_count example:

```
import pandas as pd
from protloc_mex1.AA_count import dna_sequence_conduct, rna_sequence_conduct, protein_sequence_conduct

# Example DataFrame with DNA sequences
df_dna = pd.DataFrame({
    'gene_seq': ['ATCGTGCA', 'TGCTAGCT', 'CTAGCTAG']
})

# Call the dna_sequence_conduct function
df_dna_processed = dna_sequence_conduct(df_dna, 'gene_seq')
print(df_dna_processed)

# Assume you have a DataFrame containing RNA sequences
df_rna = pd.DataFrame({
    'gene_seq': ['AUCGUGCA', 'UGCUAGCU', 'CUAGCUAG']
})

# Call the rna_sequence_conduct function
df_rna_processed = rna_sequence_conduct(df_rna, 'gene_seq')
print(df_rna_processed)

# Assume you have a DataFrame containing protein sequences
df_protein = pd.DataFrame({
    'Sequence': ['ACDEFGHIKLMNPQRSTVWY', 'ACDEFGHIKLMNPQRSTVWY']
})

# Call the protein_sequence_conduct function
df_protein_processed = protein_sequence_conduct(df_protein, 'Sequence')
print(df_protein_processed)

```

### GO_count

GO_count are capability in using Doc2vec to get GO representation，for initialize model can see below：

```
import gensim
from gensim.models.doc2vec import Doc2Vec
from protloc_mex1.GO_count import GO_pre_Process, model_training, vec_create_GO

# Create dummy data
data = pd.DataFrame({
    'Entry': ['Gene1', 'Gene2', 'Gene3'],
    'GO_BP': ['some document GO:0008150', 'some document GO:0008150;GO:0009987', 'some document GO:0009987'],
    'GO_MF': ['some document GO:0003674', 'some document GO:0003674;GO:0003824', 'some document GO:0003824']
})

# Preprocess data
data = GO_pre_Process(data, '\[GO:\d+\]', 'GO_BP')
data = GO_pre_Process(data, '\[GO:\d+\]', 'GO_MF')

# Initialize models
BP_model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40, window=5, workers=1, dm=0, seed=0)
MF_model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40, window=5, workers=1, dm=0, seed=0)

# Train models
BP_model_trained = model_training(data, BP_model, 'GO_BP')
MF_model_trained = model_training(data, MF_model, 'GO_MF')

# Generate word vectors
BP_data = vec_create_GO(data, BP_model_trained, 'GO_BP')
MF_data = vec_create_GO(data, MF_model_trained, 'GO_MF')

# Print word vectors
print(BP_data)
print(MF_data)

```



## Supplementary materials

All supplementary materials associated with the article can be found in the Supplementary_material folder. Furthermore, the code and detailed explanations related to the two experimental research cases mentioned in the article, Case 1 and Case 2, are available in their respective directories.

The subcellular localization classification models trained for Case 1 and Case 2 are stored separately in <Case1/Classification and feature filtering module/csae1_localization_model.pkl> and <Case2/Classification and feature filtering module/csae1_localization_model.pkl>. These models accept protein feature inputs identical to those in the demo file and generate corresponding predictions.

## Citation

As the manuscript is currently under review,  If you require any help, please contact the author via email at 1024226968@qq.com.

### Acknowledgments

we are acknowledge the contributions of the open-source community and the 

developers of the Python libraries used in this study. 
