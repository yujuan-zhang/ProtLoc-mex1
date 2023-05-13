# ProtLoc-Mex1

## Introduction ProtLoc-Mex1

This project offers a comprehensive pipeline for the rapid development of subcellular localization prediction and model interpretation. It encompasses 42 amino acid feature characterization algorithms and Gene Ontology (GO) feature extraction based on the Doc2Vec approach. Additionally, two random forest models for protein localization prediction are provided. 

with support by SHAP package warped into ProtLoc-mex1 module，everyone can easily use two random forest models above to get the global explanation and local explanation of the feature (physiochemical characteristics of amino acid sequence and GO annotation semantics)  and model in  protein localization prediction.

## Installation 

The core code of this project has been uploaded to the PyPI repository. To obtain it, please execute the following command:

```
pip install protloc_mex1
```

### Dependencies

ProtLoc-Mex1 requires Python  >= 3.9.

Below are the Python packages required by ProtLoc-Mex1, which are automatically installed with it:

```
dependencies = [
        "biopython~=1.79",
        "numpy>=1.20.3",
        "pandas>=1.4.1",
        "seaborn>=0.11.2",
        "matplotlib>=3.5.1",
        "shap~=0.41.0",
]
```

 and other not automatically installed but also required Python packages：

```
dependencies = [
       "scikit-learn>=1.0.2",
       "gensim>=4.2.0"
]
```

## Supplementary materials

All supplementary materials associated with the article can be found in the Supplementary_material folder. Furthermore, the code and detailed explanations related to the two experimental research cases mentioned in the article, Case 1 and Case 2, are available in their respective directories.

The subcellular localization classification models trained for Case 1 and Case 2 are stored separately in <Case1/Classification and feature filtering module/csae1_localization_model.pkl> and <Case2/Classification and feature filtering module/csae1_localization_model.pkl>. These models accept protein feature inputs identical to those in the demo file and generate corresponding predictions.

## Citation

As the manuscript is currently under review, the complete core code and pre-trained models of ProtLoc-Mex1 have not been completely released. If you require access to the core code, please contact the author via email at 1024226968@qq.com.

### Acknowledgments

we are acknowledge the contributions of the open-source community and the 

developers of the Python libraries used in this study. 
