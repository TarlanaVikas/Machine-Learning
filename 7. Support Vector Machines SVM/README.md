# Support Vector Machines (SVM)

## 📌 Objective:
To use Support Vector Machines (SVM) for both linear and non-linear binary classification using the breast cancer dataset.

## 🧰 Tools and Libraries Used:
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## ⚙️ Step-by-Step Process:

### 1. Virtual Environment Setup
Ensure your virtual environment is already created and activated.

### 2. Install Required Packages
```
pip install pandas matplotlib scikit-learn numpy
```

### 3. Load Dataset
The breast cancer dataset (`breast-cancer.csv`) is loaded using Pandas.

### 4. Data Preparation
- Dropped the 'diagnosis' column as the target.
- Mapped 'M' (malignant) to 1 and 'B' (benign) to 0.

### 5. Train-Test Split
- Used `train_test_split` from sklearn to split the dataset (80% train, 20% test).

### 6. Feature Scaling
- Standardized the features using `StandardScaler` for better SVM performance.

### 7. Train Linear and RBF SVM
- Linear SVM: `SVC(kernel='linear')`
- RBF SVM: `SVC(kernel='rbf')`

### 8. Evaluate Model
- Used confusion matrix and classification report to evaluate both models.

### 9. Cross-Validation
- Performed 5-fold cross-validation using `cross_val_score`.

## 📊 Outputs
See `observations.md` for output summaries and evaluation metrics.

# Observations and Output Summary

## 📋 Dataset Overview:
- Shape: (569, 31)
- Target Variable: `diagnosis` (Mapped: M → 1, B → 0)

## 🔍 Preprocessing:
- Converted categorical labels to binary numeric values.
- Standardized all feature values.

## ⚙️ Model Results:

### 🔹 Linear SVM:
```
Confusion Matrix:
[[68  1]
 [ 3 42]]

Classification Report:
              precision    recall  f1-score   support

           0       0.96      0.99      0.97        69
           1       0.98      0.93      0.95        45

    accuracy                           0.96       114
   macro avg       0.97      0.96      0.96       114
weighted avg       0.96      0.96      0.96       114
```

- Cross-Validation Accuracy (Linear): ~0.97

### 🔹 RBF SVM:
```
Confusion Matrix:
[[68  1]
 [ 1 44]]

Classification Report:
              precision    recall  f1-score   support

           0       0.99      0.99      0.99        69
           1       0.98      0.98      0.98        45

    accuracy                           0.98       114
   macro avg       0.98      0.98      0.98       114
weighted avg       0.98      0.98      0.98       114
```

- Cross-Validation Accuracy (RBF): ~0.98

## ✅ Key Takeaways:
- Both models performed very well, with RBF slightly outperforming Linear SVM.
- The RBF kernel can capture non-linear patterns better than linear.
- SVM is highly effective for binary classification when features are standardized.

## ✅ Conclusion:
This task demonstrated how to implement and evaluate both linear and non-linear SVMs, interpret their performance, and understand decision boundaries.
