# 🧪 Observations from Logistic Regression on Breast Cancer Dataset

## 📊 Dataset Overview:
- Dataset: Breast Cancer Wisconsin Diagnostic Data (`data.csv`)
- Rows: 569
- Columns: 33 → Dropped `Unnamed: 32` and `id` columns
- Target variable: `diagnosis` (M = Malignant, B = Benign) → Encoded as 1 (M) and 0 (B)

## 🔍 Preprocessing Steps:
- Dropped irrelevant columns: `Unnamed: 32`, `id`
- Encoded diagnosis into binary
- Standardized features using `StandardScaler`
- Train-Test Split: 80% training, 20% testing

## 📈 Model Used:
- Logistic Regression (Binary Classification)
- Tool: `sklearn.linear_model.LogisticRegression`

## ✅ Evaluation Metrics:
- **Confusion Matrix**:
  - True Positives: High
  - False Positives/Negatives: Low → good performance

- **Classification Report**:
  - Precision, Recall, and F1-score are all high (close to 1)
  - Model is strong at distinguishing malignant from benign tumors

- **ROC-AUC Score**:
  - ROC-AUC ≈ Very close to 1 → excellent classifier

- **ROC Curve**:
  - Smooth curve with high TPR and low FPR
  - Area under curve confirms high accuracy

## 📌 Inference:
- Logistic Regression performs very well on this dataset.
- Most features are informative and relevant.
- No need for feature reduction for basic classification.
- Could experiment with regularization (L1/L2), or test other classifiers (e.g., Random Forest) in the future.