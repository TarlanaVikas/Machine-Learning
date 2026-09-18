# Task 7: Support Vector Machines (SVM)

## 📌 Objective:
To use Support Vector Machines (SVM) for both linear and non-linear binary classification using the breast cancer dataset.

## 🧰 Tools and Libraries Used:
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## 📁 Folder Structure:
```
AIML Internship/
└── Task 7/
    ├── venv/
    ├── breast-cancer.csv
    └── main.py
```

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

## ✅ Conclusion:
This task demonstrated how to implement and evaluate both linear and non-linear SVMs, interpret their performance, and understand decision boundaries.