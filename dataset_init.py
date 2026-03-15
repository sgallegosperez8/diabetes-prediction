#mport kagglehub
import pandas as pd

"""
#kagglehub was used to download the dataset 
# Download latest version
path = kagglehub.dataset_download("iammustafatz/diabetes-prediction-dataset")

print("Path to dataset files:", path)
"""
diabetes = pd.read_csv("diabetes_prediction_dataset.csv")
diabetes
diabetes.columns
diabetes.size
diabetes.shape