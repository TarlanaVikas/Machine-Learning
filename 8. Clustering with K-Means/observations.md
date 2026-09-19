# 🔎 Task 8 Observations – K-Means Clustering

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