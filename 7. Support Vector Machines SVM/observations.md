# Task 7: Observations and Output Summary

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