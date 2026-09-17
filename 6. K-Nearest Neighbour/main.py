# 1. Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load the dataset
df = pd.read_csv("Iris.csv")

# 3. Basic info
print("Initial Dataset Info:\n")
print(df.info())
print(df.head())

# 4. Drop unnecessary columns (Id column here)
df = df.drop(columns=["Id"])

# 5. Separate features and target
X = df.drop("Species", axis=1)
y = df["Species"]

# 6. Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 7. Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 8. Train and test KNN with different values of K
k_values = [1, 3, 5, 7]
for k in k_values:
    print(f"\nResults for k={k}")
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

# 9. Optional: Visualize using seaborn pairplot
sns.pairplot(df, hue="Species")
plt.suptitle("Iris Data - Pairplot", y=1.02)
plt.show()
