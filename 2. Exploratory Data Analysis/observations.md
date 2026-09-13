## 1. Summary Statistics Observations
- **Age** has a mean of approximately **29.70 years** and a median of **28 years**, indicating a slightly right-skewed distribution.
- **Fare** has a mean of around **32.20**, but the presence of a very high maximum fare (~512) suggests **significant outliers**.
- **SibSp** and **Parch** mostly have values around **0**, showing most passengers traveled alone or with very few relatives.
- **Survived** shows that about **38% survived**, suggesting a survival imbalance.
- **Pclass** is skewed towards **3rd class** passengers.

## 2. Histograms Observations
- **Age distribution** is unimodal but slightly **right-skewed**; most passengers are between **20–40 years**.
- **Fare** shows an extreme **right skew** with a few passengers paying exceptionally high fares.
- **Pclass** shows the majority are **3rd class** passengers.
- **Survival** is somewhat imbalanced (more 0s).

## 3. Boxplots Observations
- **Fare** has **many outliers**, especially in higher ranges (>200).
- **Age** has mild outliers at both very young (infants) and very old ages.
- **SibSp** and **Parch** have **lots of zeros** and occasional large values, showing most traveled alone but some with large families.

## 4. Pairplot Observations
- **Pclass** and **Fare** are negatively related: higher classes (1st class) paid much higher fares.
- **Sex** and **Survival** have an evident pattern — females had higher survival rates.
- **Age** and **Survival** have a slight trend: very young children had higher survival.
- Clusters are visible for **Fare** based on Pclass.

## 5. Correlation Heatmap Observations
- **Fare** and **Pclass** have a strong **negative correlation** (~ -0.55).
- **SibSp** and **Parch** have a moderate **positive correlation** (~0.41), suggesting families traveling together.
- **Survived** correlates positively with **Fare** and negatively with **Pclass**.
- **Sex** (after encoding) shows a correlation with **Survived**.

---

# Key Patterns and Anomalies:
- **Positive Pattern:** Higher fare passengers (1st class) had better survival rates.
- **Anomaly:** Extremely high fare outliers (~512) could belong to a few VIP or group tickets.
- **Anomaly:** Some passengers had **7 siblings/spouses** traveling with them — unusual compared to the rest.

Awesome! 🚀  
Here’s your **final step: "Feature-Level Inferences"**, properly written and polished for `observations.md`:

---

# ✨ Feature-Level Inferences

| Feature      | Inference |
|--------------|-----------|
| **Pclass**   | Higher-class passengers (1st class) had much better survival chances than 3rd class passengers. Socioeconomic status was a strong survival factor. |
| **Sex**      | Females had a significantly higher survival rate compared to males, indicating "women and children first" policy impact. |
| **Age**      | Very young children had higher survival rates. Adults between 20-40 had mixed outcomes. Older passengers (>60) had lower survival chances. |
| **Fare**     | Passengers who paid higher fares (usually 1st class) had better survival outcomes. Fare is a strong indirect survival predictor. |
| **SibSp & Parch** | Having small family groups (1-2 siblings/parents) slightly improved survival chances. Very large groups had poorer survival outcomes. |
| **Embarked** | Passengers boarding from port 'C' (Cherbourg) had slightly higher survival rates compared to 'S' (Southampton) and 'Q' (Queenstown). |
| **Cabin**    | Missing cabin information (most 3rd class passengers) correlates with lower survival, while known cabins (mostly 1st class) correlate with better survival. |