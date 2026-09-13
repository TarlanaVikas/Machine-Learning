# 📝 Titanic Dataset - Exploratory Data Analysis (EDA)

## 📚 Objective
Perform **Exploratory Data Analysis** on the Titanic dataset to understand the data through statistics and visualizations.

---

## 🛠 Tools Used
- **Python** (3.12)
- **VS Code** (Editor)
- **Libraries**:
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn

---

## 📁 Project Setup

1. **Created a project folder:**  
   ➔ `Task2_EDA`
2. **Created a Python virtual environment:**  
   ```bash
   python -m venv venv
   ```
3. **Activated the virtual environment:**  
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
4. **Installed necessary libraries:**
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
5. **Downloaded Titanic Dataset** from Kaggle and saved it inside the project folder as `titanic.csv`.
6. **Created main code file:**  
   ➔ `main.py`

---

## 🧹 Data Loading

- Imported the dataset using Pandas:
  ```python
  df = pd.read_csv('titanic.csv')
  ```
- Checked basic info:
  ```python
  df.info()
  df.head()
  ```

---

## 📊 EDA Steps

### 1. **Generated Summary Statistics**
- Used:
  ```python
  df.describe()
  ```
- Observed:
  - Count, mean, median, standard deviation, min, max for numerical features.

---

### 2. **Visualized Histograms for Numerical Features**
- Used Matplotlib and Seaborn to plot histograms for:
  - Age
  - Fare
  - SibSp
  - Parch

Example:
```python
df['Age'].hist()
plt.show()
```

---

### 3. **Created Boxplots**
- Created boxplots to detect **outliers**:
  ```python
  sns.boxplot(x=df['Fare'])
  plt.show()
  ```

---

### 4. **Pairplot and Correlation Matrix**
- Created a pairplot:
  ```python
  sns.pairplot(df, hue='Survived')
  plt.show()
  ```
- Created a correlation heatmap:
  ```python
  sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
  plt.show()
  ```

---

## 📈 Observations

- Summarized all findings from each step into a detailed file:  
  ➔ `observations.md`
- Included:
  - Summary Statistics
  - Histograms Observations
  - Boxplots Observations
  - Pairplot Observations
  - Correlation Observations
  - Key Patterns and Anomalies
  - Final Feature-Level Inferences

---

## 📝 Final Note
- Successfully performed full EDA manually using Python scripts (no Jupyter Notebook).
- Followed clean step-by-step modular coding and proper documentation.
- Ready to proceed to modeling or deeper insights!

---

# ✅ Status: COMPLETED