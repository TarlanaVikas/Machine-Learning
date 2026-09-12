# main.py
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv('titanic.csv')
print("Initial Data Info:")
print(df.info())
print(df.head())

# 2. Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# 3. Fill missing 'Age' with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# 4. Fill missing 'Embarked' with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 5. Drop 'Cabin' since too many missing values
df.drop(columns=['Cabin'], inplace=True)

# 6. Convert categorical to numerical
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# 7. Standardize numerical features
scaler = StandardScaler()
numerical_cols = ['Age', 'Fare']
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# 8. Visualize outliers
plt.figure(figsize=(10,5))
sns.boxplot(data=df[['Age', 'Fare']])
plt.title("Boxplots for Age & Fare")
plt.show()

# 9. Save cleaned dataset
df.to_csv('cleaned_titanic.csv', index=False)
print("Cleaned dataset saved as 'cleaned_titanic.csv'")
