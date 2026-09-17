# 🌸 Task 6 - K-Nearest Neighbors (KNN) Classification

## 📌 Objective

The goal of this task is to **implement the K-Nearest Neighbors (KNN) algorithm** using the **Iris dataset**, understand how the algorithm works for classification problems, evaluate model performance, and visualize insights from the dataset.

---

## 🧰 Tools & Libraries Used

- **Python 3**
- **Pandas** – For data manipulation and preprocessing
- **Scikit-learn** – For modeling (KNN, preprocessing, metrics)
- **Matplotlib & Seaborn** – For data visualization

---

## 🗂 Project Structure

Task 6 - KNN/
│
├── Iris.csv # Dataset
├── main.py # Main script containing code
└── README.md # Project documentation

---

## 📈 Dataset Description: *Iris.csv*

- **Total Rows:** 150
- **Features:**
  - SepalLengthCm
  - SepalWidthCm
  - PetalLengthCm
  - PetalWidthCm
- **Target:**
  - Species (Iris-setosa, Iris-versicolor, Iris-virginica)

---

## 🔍 Step-by-Step Process

### 1. Setup

- Created a folder `Task 6 - KNN`
- Created and activated a virtual environment:
  ```bash
  python -m venv venv
  venv\Scripts\activate
- Installed necessary libraries: pip install pandas matplotlib seaborn scikit-learn

### 2. Load & Explore Dataset

- Loaded the dataset using pandas
- Viewed structure using .info() and .head()
- Dropped the Id column as it does not contribute to classification

### 3. Data Preprocessing

- Split dataset into features (X) and target (y)
- Standardized features using StandardScaler to ensure equal weighting for distance computation in KNN

### 4. Train-Test Split

Split data into 80% training and 20% testing sets using train_test_split

### 5. KNN Classification

- Trained KNeighborsClassifier with multiple values of K: k = 1, 3, 5, 7
- For each K, printed:
   - Accuracy score
   - Confusion matrix
   - Classification report (precision, recall, f1-score)

### 6. Data Visualization
Used Seaborn's pairplot to visualize feature relationships and natural class separations between flower species.

### 📊 Sample Output (for K = 3)

Accuracy: 1.0

Confusion Matrix:
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]

Classification Report:
              precision    recall  f1-score   support

    setosa       1.00      1.00      1.00        10
versicolor       1.00      1.00      1.00        10
 virginica       1.00      1.00      1.00        10

accuracy                           1.00        30

### 🎯 Observations & Learnings

- Feature Scaling is crucial in KNN as it is a distance-based algorithm.
- Lower values of K can lead to overfitting, while higher values might underfit.
- The Iris dataset has well-separated classes, making KNN highly effective.
- Pairplot visualization clearly showed how petal dimensions separate the species better than sepal dimensions.