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