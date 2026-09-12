
# Data Preprocessing Notes

This document outlines the steps taken to preprocess the Titanic dataset for machine learning or analysis purposes.

---

### 1. **Load the Dataset**
   - **Objective**: Import the raw dataset into Python using `pandas`.
   - **Method**:
     ```python
     df = pd.read_csv('titanic.csv')
     ```
   - **Explanation**: The dataset is loaded from a CSV file into a `pandas` DataFrame to perform further operations.

---

### 2. **Explore Basic Info**
   - **Objective**: Understand the structure of the data, including data types, number of missing values, and a preview of the first few rows.
   - **Method**:
     ```python
     print(df.info())
     print(df.head())
     ```
   - **Explanation**: The `info()` function provides a summary of the DataFrame, including column types and null counts. The `head()` method shows the first few rows to understand the data format.

---

### 3. **Check Missing Values**
   - **Objective**: Identify any missing values in the dataset.
   - **Method**:
     ```python
     print(df.isnull().sum())
     ```
   - **Explanation**: The `isnull()` function detects null values in the dataset, and `sum()` gives the total number of missing values per column.

---

### 4. **Handle Missing Values**
   - **Objective**: Fill or drop missing values to make the dataset complete.
     - **Age**: Filled with the **median** (for numerical columns).
     - **Embarked**: Filled with the **mode** (for categorical columns).
     - **Cabin**: Dropped due to too many missing values.
   - **Methods**:
     ```python
     df['Age'].fillna(df['Age'].median(), inplace=True)
     df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
     df.drop(columns=['Cabin'], inplace=True)
     ```
   - **Explanation**: Missing numerical values (like `Age`) are filled with the median to avoid skewing the data. Missing categorical values (like `Embarked`) are filled with the mode. The "Cabin" column is dropped as it has too many missing values.

---

### 5. **Convert Categorical Features to Numerical**
   - **Objective**: Convert categorical variables to numerical values using **one-hot encoding**.
   - **Method**:
     ```python
     df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
     ```
   - **Explanation**: One-hot encoding is applied to the `Sex` and `Embarked` columns, converting them into binary columns. The `drop_first=True` argument ensures that we avoid the dummy variable trap by dropping one of the categories for each feature.

---

### 6. **Standardize Numerical Features**
   - **Objective**: Scale numerical features to have a mean of 0 and a standard deviation of 1, ensuring that features are on the same scale.
   - **Method**:
     ```python
     from sklearn.preprocessing import StandardScaler
     scaler = StandardScaler()
     numerical_cols = ['Age', 'Fare']
     df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
     ```
   - **Explanation**: `StandardScaler` is used to standardize the `Age` and `Fare` columns, making them more suitable for machine learning algorithms that are sensitive to feature scales (e.g., logistic regression, SVMs).

---

### 7. **Visualize Outliers**
   - **Objective**: Use boxplots to detect and visualize any potential outliers in numerical columns.
   - **Method**:
     ```python
     import matplotlib.pyplot as plt
     import seaborn as sns
     plt.figure(figsize=(10,5))
     sns.boxplot(data=df[['Age', 'Fare']])
     plt.title("Boxplots for Age & Fare")
     plt.show()
     ```
   - **Explanation**: Boxplots are a great way to visualize outliers. Outliers are typically shown as points outside the "whiskers" of the plot.

---

### 8. **Save the Cleaned Dataset**
   - **Objective**: Save the preprocessed dataset to a new CSV file for future use or model building.
   - **Method**:
     ```python
     df.to_csv('cleaned_titanic.csv', index=False)
     ```
   - **Explanation**: After completing all the necessary preprocessing steps, the cleaned dataset is saved as a new file (`cleaned_titanic.csv`) to ensure that the changes are stored and can be used later.

---

### Summary

These steps ensure that the dataset is clean and ready for machine learning tasks. The data preprocessing steps you’ve taken—handling missing values, encoding categorical variables, standardizing numerical features, and visualizing outliers—are foundational for building robust machine learning models.