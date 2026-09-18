import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load dataset
df = pd.read_csv('breast-cancer.csv')
print("Initial Dataset Shape:", df.shape)
print(df.head())

# Step 2: Prepare features & target
X = df.drop('diagnosis', axis=1)
y = df['diagnosis'].map({'B': 0, 'M': 1})  # Convert labels to 0 and 1

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Train Linear SVM
linear_svm = SVC(kernel='linear', C=1)
linear_svm.fit(X_train_scaled, y_train)
y_pred_linear = linear_svm.predict(X_test_scaled)

# Step 6: Train RBF SVM
rbf_svm = SVC(kernel='rbf', C=1, gamma='scale')
rbf_svm.fit(X_train_scaled, y_train)
y_pred_rbf = rbf_svm.predict(X_test_scaled)

# Step 7: Evaluation
print("\n--- Linear SVM ---")
print(confusion_matrix(y_test, y_pred_linear))
print(classification_report(y_test, y_pred_linear))

print("\n--- RBF SVM ---")
print(confusion_matrix(y_test, y_pred_rbf))
print(classification_report(y_test, y_pred_rbf))

# Step 8: Cross-validation scores
linear_scores = cross_val_score(linear_svm, X_train_scaled, y_train, cv=5)
rbf_scores = cross_val_score(rbf_svm, X_train_scaled, y_train, cv=5)

print(f"\nCross-Validation Accuracy (Linear): {np.mean(linear_scores):.2f}")
print(f"Cross-Validation Accuracy (RBF): {np.mean(rbf_scores):.2f}")