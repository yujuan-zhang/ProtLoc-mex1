

# Import required libraries
import os
import pandas as pd
import numpy as np
import joblib

# Set file paths for input and output directories
open_path=r"D:\Githubfolder\ProtLoc-mexl\Case1\Classification and feature filtering module"
save_path=r"D:\Githubfolder\ProtLoc-mexl\Case1\Classification and feature filtering module\output"

# Check if the output directory exists, and create it if it does not exist
if os.path.isdir(save_path):
    pass
else:
    os.makedirs(save_path)

# Load the trained classification model from the input directory
model_pipe= joblib.load(open_path+"/"+'csae1_localization_model.pkl')

# Extract the trained model from the pipeline object
model=model_pipe.named_steps['Model']

# Load the demo dataset from the input directory
demo_data=pd.read_csv(open_path+"/"+'demo_dataframe.csv',header=0,sep=",",index_col="ID")

# Separate the feature columns from the target column in the demo dataset
X_demo=demo_data.drop(columns='type')  
y_demo=demo_data['type'] 

# Use the trained model to predict the target labels for the demo dataset
X_demo_hat=pd.DataFrame(model.predict(np.array(X_demo)),columns=["predict"],
                   index=X_demo.index)

# Concatenate the original feature columns, target column, and predicted target column into a new dataframe
X_demo_save = pd.concat([X_demo, y_demo, X_demo_hat], axis=1)


