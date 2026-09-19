# 🧠 Task 8: K-Means Clustering – AIML Internship

## 🎯 Objective
Use K-Means clustering to identify customer segments based on Annual Income and Spending Score from the Mall Customers dataset.

---

## 📁 Folder Structure
AIML_Task8_KMeans/
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
    mkdir AIML_Task8_KMeans
    cd AIML_Task8_KMeans
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

## ✅ Task Completed!
Successfully implemented customer segmentation using KMeans clustering.