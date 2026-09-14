# Linear Regression on Housing Dataset

## 📚 Objective:
The goal of this project was to understand and implement **Simple and Multiple Linear Regression** using Scikit-learn, Pandas, and Matplotlib.

---

## 🛠️ Steps Followed:

### 1. **Folder Setup**
- Created a new project folder named `Task3-LinearRegression`.
- Set up a virtual environment (`venv`) using: python -m venv venv
- Activated the virtual environment.
- Installed required libraries: pip install pandas numpy matplotlib scikit-learn

- Downloaded the dataset `Housing.csv` and placed it in the project folder.

---

### 2. **Script Development (main.py)**

- **Imported** essential libraries:
- pandas
- numpy
- matplotlib.pyplot
- sklearn.model_selection
- sklearn.linear_model
- sklearn.metrics

- **Loaded** the dataset using Pandas and explored:
- First few rows.
- Info about columns and data types.
- Checked for missing values.

- **Selected** features (`area`, `bedrooms`, `bathrooms`, `stories`, `parking`) and target (`price`).

- **Split** the dataset into training and testing sets using `train_test_split` (80%-20%).

- **Trained** a Linear Regression model using `LinearRegression()` from Scikit-learn.

- **Made Predictions** on the test set.

- **Evaluated** the model using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

- **Visualized** the relationship between `Area` and `Price`:
- Plotted both actual and predicted prices.

- **Printed** model intercept and coefficients for interpretation.

---
# Observations: Linear Regression on Housing Dataset

## 📈 1. Summary of Dataset
- Total Records: ~500
- Key Numeric Features: Area, Bedrooms, Bathrooms, Stories, Parking
- Target Feature: Price

---

## 🔍 2. Model Performance

| Metric | Value |
|:------|:------|
| Mean Absolute Error (MAE) | (value printed during run) |
| Mean Squared Error (MSE) | (value printed during run) |
| R² Score | (value printed during run) |

**Interpretation**:  
- A higher R² value close to 1 indicates a good fit.
- Low MAE and MSE indicate accurate predictions.

---

## 📊 3. Feature Coefficients

| Feature | Coefficient | Interpretation |
|:--------|:------------|:---------------|
| Area | (value) | Higher area leads to increase in price. |
| Bedrooms | (value) | More bedrooms generally increase price, but not always linearly. |
| Bathrooms | (value) | More bathrooms positively affect price. |
| Stories | (value) | More stories slightly impact the price. |
| Parking | (value) | More parking space adds to price moderately. |

---

## 🚩 4. Key Insights
- **Area** is the most significant factor influencing house price.
- **Parking** also moderately increases the house value.
- Features like **stories** and **bathrooms** have secondary but still notable impact.
- **Bedrooms** have variable impact (may depend on quality/location).

---

## 📚 Learnings:
- Linear Regression assumes linear relationships between input and output.
- Importance of preprocessing data (handling missing values if any).
- Understanding metrics like MAE, MSE, and R² to evaluate models.
---

## 🖼️ Libraries Used:
- Pandas
- Numpy
- Matplotlib
- Scikit-learn

---

## 📊 Output:
- Displayed evaluation metrics (MAE, MSE, R²).
- Displayed a scatter plot showing how well the model predicts housing prices.
- Interpreted which features most influenced the house price prediction.

---

## 🏁 Conclusion:
Successfully implemented and understood:
- How to perform Linear Regression.
- How to split data into train/test.
- How to evaluate model performance.
- How to interpret coefficients to understand feature importance.
