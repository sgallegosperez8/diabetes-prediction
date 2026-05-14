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

