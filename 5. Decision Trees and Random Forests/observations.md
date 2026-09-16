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