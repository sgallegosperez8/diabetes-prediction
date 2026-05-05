# diabetes-prediction

Predicting Diabetic Status Among Females: A Logistic Regression Analysis of Clinical Indicators and Age-Based Data Gaps

[diabetes_prediction_dataset.csv](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)

## Project Motivation

Diabetes is a chronic metabolic disease reaching epidemic proportions in the United States, with a higher prevalence observed in women. Despite this, there is insufficient research into how specific demographic and medical factors influence the diabetic status of women. This study aims to:  
+1

Identify Key Patterns: Understand the differences between diabetic and non-diabetic female patients.  

Discover Relationships: Analyze correlations between health factors like BMI, age, and glucose levels.  

Improve Diagnosis: Build an accurate predictive model to facilitate faster clinical intervention.  
+1

## Methodology
1. Data Inspection and Cleaning

The analysis utilized the diabetes_dataset_prediction_csv, containing 100,000 records and 9 features.  

Filtering: The data was specifically filtered to focus on female participants.  

De-duplication: 3,854 duplicate records were identified and removed.  

Handling Nulls: No null or missing values were found in the original set.  

Feature Engineering: The smoking_history feature was simplified from phrases to single words and then numerically encoded.  

## Exploratory Data Analysis (EDA)

EDA revealed significant trends and data gaps:

Age Disparity: There was a "left-skewed" distribution, with significantly more data for women over 45 compared to girls under 18.  

Correlation: Blood glucose levels (0.43) and HbA1c levels (0.42) showed the strongest positive correlation with diabetes status.  
+1

BMI: Body Mass Index was identified as the second-highest correlation factor (0.24).  

3. Modeling

A supervised machine learning approach was chosen to model the binomial outcome (1 for Diabetic, 0 for Non-Diabetic).  
+1

Algorithm: Logistic Regression (specifically LogisticRegressionCV) was selected as the best fit for the binomial response variable.  
+2

Preprocessing: Features were scaled using StandardScaler() to ensure uniform weight.  
+1

Training: An 80/20 train-test split was used with a stratify parameter to maintain class proportions.  

Cross-Validation: 5-Fold cross-validation was employed, and class_weight="balanced" was applied to handle the unbalanced nature of the dataset.  
+1

## Evaluations

The model's performance was measured using several metrics to ensure accuracy despite the data imbalance:

Accuracy: The model achieved an overall accuracy of 89%.  

ROC Curve: The Area Under the Curve (AUC) was 0.95, indicating a high true-positive rate with a low false-positive rate.  

Confusion Matrix:

True Positives: 594.  

True Negatives: 5,821.  

False Positives: 673.  

False Negatives: 104.  

## Conclusions
The study confirms that HbA1c and blood glucose levels are the primary indicators of diabetes in women across all age groups. However, significant data gaps exist for females under 18, suggesting a critical need for further research in younger demographics to improve early disease prediction.

