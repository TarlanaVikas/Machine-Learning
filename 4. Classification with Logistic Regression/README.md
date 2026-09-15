# Classification with Logistic Regression

## 📚 Objective:
Build a binary classifier using Logistic Regression to predict whether a tumor is **malignant** or **benign** using the Breast Cancer dataset.

---

## 🛠 Tools Used:
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📁 Folder Setup:
AIML Internship/ └── Task 4/ ├── data.csv ├── main.py ├── observations.md └── README.md


---

## ⚙️ Steps Performed:

1. **Created a virtual environment** and activated it:
   ```bash
   python -m venv venv
   venv\Scripts\activate

2. **Installed dependencies:**
   pip install pandas scikit-learn matplotlib seaborn

3. Created main.py with the full logistic regression code.

4. **Preprocessed the dataset:**
   - Dropped unnecessary columns (Unnamed: 32, id)
   - Converted target labels M/B to 1/0
   - Standardized features using StandardScaler

5. **Trained the Logistic Regression model:**
   - Split data into training (80%) and testing (20%)
   - Fit model on training data

6. **Evaluated the model:**
   - Printed confusion matrix & classification report
   - Calculated ROC-AUC score
   - Plotted ROC Curve

7. Documented insights in observations.md

## ✅ Outcome:
Achieved a high accuracy and ROC-AUC score. The model is effective in classifying tumor types using basic logistic regression.
