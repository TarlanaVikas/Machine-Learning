# Task 5: Decision Trees and Random Forests

## 📌 Objective
Learn and implement tree-based machine learning models (Decision Tree & Random Forest) for classification tasks using the Heart Disease dataset.

---

## 📁 Folder Structure
task_5_decision_trees/
│
├── heart.csv
├── main.py
├── README.md
└── observations.md

---

## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Graphviz (optional, for advanced tree visualizations)

---

## 🧰 Installation

Activate your virtual environment and run:

```bash
(pip install pandas scikit-learn matplotlib seaborn graphviz)

---

## 🔍 Steps Performed

- Created project folder task_5_decision_trees and placed heart.csv inside it.
- Created a main.py file and wrote step-by-step code.
- Imported required libraries for EDA, model building, and evaluation.
- Loaded the heart disease dataset using pandas. 
- Split the dataset into training and test sets (80/20 split). 
- Trained a Decision Tree Classifier with max_depth=4 and visualized it using plot_tree().
- Evaluated the Decision Tree with accuracy, confusion matrix, and classification report. 
- Trained a Random Forest Classifier with 100 trees and compared results.
- Plotted feature importances for the Random Forest model.
- Performed cross-validation to check model reliability across folds.

---

## ✅ Output Highlights
1. Decision Tree & Random Forest were trained and evaluated. 

2. Accuracy scores and classification metrics compared.

3. Important features affecting prediction were visualized.

---

## 📂 How to Run
python main.py
This will:
- Train both classifiers
- Print evaluation metrics
- Show visualizations (Decision Tree and Feature Importance)


---

### 📊 `observations.md`

```markdown
# Observations – Task 5: Decision Trees & Random Forests

## Dataset Overview
- **Dataset**: Heart Disease Prediction
- **Rows**: 1025
- **Columns**: 14
- **Target Variable**: `target` (Binary – 0: No disease, 1: Disease)

---

## Model 1: Decision Tree

### Configuration
- `max_depth = 4`

### Evaluation
- **Accuracy**: ~0.80
- **Confusion Matrix** showed a reasonable balance of true positives and negatives.
- Good for interpretability but can overfit if not pruned or controlled.

---

## Model 2: Random Forest

### Configuration
- `n_estimators = 100` (number of trees)

### Evaluation
- **Accuracy**: Slightly higher than Decision Tree (~0.83)
- **Better generalization** due to ensembling.
- **Feature importance plot** revealed key predictors like:
  - `cp` (chest pain type)
  - `thalach` (max heart rate)
  - `exang` (exercise-induced angina)

---

## Feature Importance (Top 5)

| Feature        | Importance |
|----------------|------------|
| `cp`           | High       |
| `thalach`      | High       |
| `exang`        | Moderate   |
| `oldpeak`      | Moderate   |
| `slope`        | Moderate   |

---

## Cross-Validation

- 5-fold cross-validation showed consistent performance.
- Mean CV accuracy: ~0.82

---

## Summary

- **Decision Trees** offer transparency and are easy to interpret.
- **Random Forests** provide higher accuracy and stability.
- **Chest pain type, heart rate, and angina** are significant indicators of heart disease.