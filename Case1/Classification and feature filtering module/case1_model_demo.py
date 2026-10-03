

# Import required libraries
from pathlib import Path
import pandas as pd
import numpy as np
import joblib

# Resolve bundled data beside this script, independent of the working directory.
open_path = Path(__file__).resolve().parent
save_path = open_path / 'output'
save_path.mkdir(parents=True, exist_ok=True)

# Load the trained classification model from the input directory
model_pipe= joblib.load(open_path / 'csae1_localization_model.pkl')

# Extract the trained model from the pipeline object
model=model_pipe.named_steps['Model']

# Load the demo dataset from the input directory
demo_data=pd.read_csv(open_path / 'demo_dataframe.csv',header=0,sep=",",index_col="ID")

# Separate the feature columns from the target column in the demo dataset
X_demo=demo_data.drop(columns='type')  
y_demo=demo_data['type'] 

# Use the trained model to predict the target labels for the demo dataset
X_demo_hat=pd.DataFrame(model.predict(np.array(X_demo)),columns=["predict"],
                   index=X_demo.index)

# Concatenate the original feature columns, target column, and predicted target column into a new dataframe
X_demo_save = pd.concat([X_demo, y_demo, X_demo_hat], axis=1)




output_file = save_path / 'demo_predictions.csv'
X_demo_save.to_csv(output_file, index_label='ID')
print(f'Saved {len(X_demo_save)} predictions to {output_file}')
