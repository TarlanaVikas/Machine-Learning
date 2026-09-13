import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv('titanic.csv')

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Summary for categorical features
print("\nCategorical Feature Summary:")
print(df.describe(include=['object']))

# Plot histograms for numeric features
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_columns:
    plt.figure(figsize=(8, 4))
    plt.hist(df[col], bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Plot boxplots for numeric features
for col in numeric_columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col], color='lightgreen')
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.grid(True)
    plt.show()

# Pairplot for numeric features
sns.pairplot(df[numeric_columns])
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.show()

# Correlation matrix
corr_matrix = df[numeric_columns].corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap of Numeric Features")
plt.show()
