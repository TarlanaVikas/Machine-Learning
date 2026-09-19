# K-Means Clustering 

## 🎯 Objective
Use K-Means clustering to identify customer segments based on Annual Income and Spending Score from the Mall Customers dataset.

---

## 📁 Folder Structure
KMeans/
│
├── venv/ # Virtual environment
├── Mall_Customers.csv # Dataset file
├── main.py # Main script for clustering
├── README.md # Step-by-step guide and explanation
└── observations.md # Outputs and insights from the task


---

## 🛠️ Tools & Libraries Used

- Python
- pandas
- matplotlib
- seaborn
- scikit-learn

---

## 📦 Setup Instructions

1. **Create Project Folder**:
    ```bash
    mkdir KMeans
    cd KMeans
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate       # For Windows
    ```

3. **Install Required Libraries**:
    ```bash
    pip install pandas matplotlib seaborn scikit-learn
    ```

4. **Add Dataset**:
    - Place the `Mall_Customers.csv` file in the project folder.

5. **Create and Run `main.py`**:
    - Copy the clustering code into `main.py`.
    - Run using:
      ```bash
      python main.py
      ```

---

## 🔍 Key Steps in Code

1. **Data Loading**: Used `pandas` to load the CSV file.
2. **Feature Selection**: Focused on `Annual Income` and `Spending Score`.
3. **Standardization**: Applied `StandardScaler` for normalization.
4. **Elbow Method**: Visualized inertia to determine optimal number of clusters (K).
5. **Model Fitting**: Fitted KMeans model with selected K.
6. **PCA Visualization**: Used PCA to reduce features to 2D and plot cluster separation.
7. **Evaluation**: Calculated Silhouette Score for cluster validation.

---

## 📈 Output Visuals

- Elbow Plot to find optimal K
- Scatter plot of PCA-reduced clusters

---

# 🔎 Observations – K-Means Clustering

## 📊 Dataset Preview

| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) |
|------------|--------|-----|--------------------|-------------------------|
| 1          | Male   | 19  | 15                 | 39                      |
| 2          | Male   | 21  | 15                 | 81                      |
| 3          | Female | 20  | 16                 | 6                       |
| ...        | ...    | ... | ...                | ...                     |

---

## 🧪 Selected Features for Clustering

- `Annual Income (k$)`
- `Spending Score (1-100)`

---

## 🔄 Preprocessing

- StandardScaler was used to normalize the selected features.
- PCA was applied for 2D visualization after clustering.

---

## 📉 Elbow Method Output

The elbow plot showed a sharp drop in inertia till K=5. After that, the curve flattened, suggesting:

> ✅ **Optimal K = 5**

---

## 🧠 KMeans Clustering Results

- Fitted KMeans model with **K=5**.
- Assigned cluster labels to each data point.
- Silhouette Score: **0.553** → indicates reasonably well-separated clusters.

---

## 📌 PCA + Cluster Visualization

A 2D scatter plot using PCA showed distinct cluster separation with minimal overlap.

- Some clusters were dense and tight (high spending, high income).
- Others were more spread out (low income, low spending, etc.).

---

## 📈 Feature Insights

- **Annual Income** and **Spending Score** successfully separated customer types:
  - Low income, low spenders
  - Low income, high spenders
  - High income, low spenders
  - High income, high spenders
  - Average income, average spenders

---

## ✅ Conclusion

- KMeans worked well on this customer segmentation task.
- PCA helped in visualizing high-dimensional clusters.
- Elbow method + Silhouette Score = reliable model evaluation.
