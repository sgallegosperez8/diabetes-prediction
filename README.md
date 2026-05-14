# diabetes-prediction machine-modeling

Predicting Diabetic Status Among Females: A Logistic Regression Analysis of Clinical Indicators and Age-Based Data Gaps

[diabetes_prediction_dataset.csv](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)

## Project Motivation

Diabetes is a chronic metabolic disease reaching epidemic proportions in the United States, with a higher prevalence observed in women. Despite this, there is insufficient research into how specific demographic and medical factors influence the diabetic status of women. This study aims to:  

+ Identify Key Patterns: Understand the differences between diabetic and non-diabetic female patients.  

+ Discover Relationships: Analyze correlations between health factors like BMI, age, and glucose levels.  

+ Improve Diagnosis: Build an accurate predictive model to facilitate faster clinical intervention.  


## Methodology
1. Data Inspection and Cleaning

The analysis utilized the diabetes_dataset_prediction_csv, containing 100,000 records and 9 features.  

+ Filtering: The data was specifically filtered to focus on female participants.  

+ De-duplication: 3,854 duplicate records were identified and removed.  

+ Handling Nulls: No null or missing values were found in the original set.  

+ Feature Engineering: The smoking_history feature was simplified from phrases to single words and then numerically encoded.  

## Exploratory Data Analysis (EDA)

EDA revealed significant trends and data gaps:

+ Age Disparity: There was a "left-skewed" distribution, with significantly more data for women over 45 compared to girls under 18.  

+ Correlation: Blood glucose levels (0.43) and HbA1c levels (0.42) showed the strongest positive correlation with diabetes status.  

+ BMI: Body Mass Index was identified as the second-highest correlation factor (0.24).  

## Modeling

A supervised machine learning approach was chosen to model the binomial outcome (1 for Diabetic, 0 for Non-Diabetic).  

+ Algorithm: Logistic Regression `LogisticRegressionCV()` was selected as the best fit for the binomial response variable.  

+ Preprocessing: Features were scaled using `StandardScaler()` to ensure uniform weight.  

+ Training: An 80/20 train-test split was used with a `stratify` parameter to maintain class proportions.  

+ Cross-Validation: 5-Fold cross-validation `cv=5`was employed, and `class_weight="balanced"` was applied to handle the unbalanced nature of the dataset.  


## Evaluations

The model's performance was measured using several metrics to ensure accuracy despite the data imbalance:

+ Accuracy: The model achieved an overall accuracy of 89%.  

+ ROC Curve: The Area Under the Curve (AUC) was 0.95, indicating a high true-positive rate with a low false-positive rate.  

+ Confusion Matrix:

 - True Positives: 594.  

 - True Negatives: 5,821.  

 - False Positives: 673.  

 - False Negatives: 104.  

## Conclusions

The study confirms that HbA1c and blood glucose levels are the primary indicators of diabetes in women across all age groups. However, significant data gaps exist for females under 18, suggesting a critical need for further research in younger demographics to improve early disease prediction.



# Diabetes Prediction in Females
### Logistic Regression Analysis of Clinical Indicators & Age-Based Data Gaps

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview
Diabetes is a chronic metabolic disease reaching epidemic proportions in the United States, with a higher prevalence observed in women. This project utilizes the [Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) to analyze how demographic and medical factors influence diabetic status, specifically focusing on data gaps within younger female demographics.

### Objectives
* **Identify Key Patterns:** Understand clinical differences between diabetic and non-diabetic female patients.
* **Correlation Discovery:** Analyze relationships between health factors like BMI, age, and glucose levels.
* **Improve Diagnosis:** Build an accurate predictive model to facilitate faster clinical intervention.

---

## Methodology & Data Pipeline

### 1. Data Inspection and Cleaning
The analysis utilized the `diabetes_prediction_dataset.csv`, containing **100,000 records** and 9 features.
* **Filtering:** The data was specifically filtered to focus on **female participants**.
* **De-duplication:** 3,854 duplicate records were identified and removed.
* **Handling Nulls:** No missing values were found in the original set.
* **Feature Engineering:** The `smoking_history` feature was simplified and numerically encoded for model compatibility.

### 2. Exploratory Data Analysis (EDA)
* **Age Disparity:** Analysis revealed a "left-skewed" distribution, with significantly more data for women over 45 compared to girls under 18.
* **Primary Drivers:** Blood glucose levels (**0.43**) and HbA1c levels (**0.42**) showed the strongest positive correlation with diabetic status.
* **BMI Influence:** Body Mass Index was the second-highest correlation factor (**0.24**).

---

## Modeling Approach

A supervised machine learning approach was chosen to model the binomial outcome ($1$ for Diabetic, $0$ for Non-Diabetic).

| Component | Choice | Rationale |
| :--- | :--- | :--- |
| **Algorithm** | `LogisticRegressionCV()` | Best fit for binomial response variables with automated cross-validation. |
| **Preprocessing** | `StandardScaler()` | Scales features to ensure uniform weight during training. |
| **Training Split** | 80/20 | Stratified split to maintain class proportions. |
| **Cross-Validation** | 5-Fold (`cv=5`) | Ensures model generalizability. |
| **Class Imbalance** | `balanced` weights | Applied to handle the unbalanced nature of the diabetic dataset. |

---

## Evaluation Metrics

The model demonstrates high sensitivity, ensuring a low rate of missed diagnoses (False Negatives).

### Performance Summary
* **Overall Accuracy:** 89%
* **ROC AUC Score:** **0.95** (Indicates excellent separation between classes).

### Confusion Matrix
| | Predicted Negative | Predicted Positive |
| :--- | :---: | :---: |
| **Actual Negative** | 5,821 (TN) | 673 (FP) |
| **Actual Positive** | 104 (FN) | 594 (TP) |

---

## Conclusions & Future Work
* **Key Finding:** HbA1c and blood glucose levels are the primary indicators of diabetes in women across all age groups.
* **Critical Need:** Significant data gaps exist for females under 18. Future research should prioritize younger demographics to improve early disease prediction and preventive care.

---

## Quick Start
```bash
# Clone the repository
git clone [https://github.com/your-username/diabetes-prediction.git](https://github.com/your-username/diabetes-prediction.git)

# Install requirements
pip install -r requirements.txt

# Run the analysis
python main.py

