### ✅ Dataset Overview

- Dataset Used: Iris Dataset
- Shape: (150, 6)
- Target Column: Species
- Features: SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm

### 🧹 Preprocessing

- Null values: None detected.
- Data types: All feature columns were floats, and the target (Species) was categorical.
- Label Encoding: The Species column was encoded as:
    - setosa → 0
    - versicolor → 1
    - virginica → 2
- Normalization: All features were scaled to a 0–1 range using MinMaxScaler.

### 📌 Model Training and Evaluation
➤ Train-Test Split
   - Split Ratio: 80% training / 20% testing
   - Train shape: (120, 4)
   - Test shape: (30, 4)

➤ KNN Training
   - Classifier Used: KNeighborsClassifier
   - Best K Value Explored: K = 3 (also experimented with 1 to 10)

➤ Performance Metrics (for K=3):
   - Accuracy: 100% on test data.
   - Confusion Matrix: 
     [[10  0  0]
     [ 0 10  0]
     [ 0  0 10]]
   - Classification Report:
     Class	Precision	Recall	F1-score	Support
     Setosa	    1.00	1.00	  1.00	     10
     Versicolor	1.00	1.00	  1.00	     10
     Virginica	1.00	1.00	  1.00	     10

### 🔍 K Value Exploration (1–10)
- Accuracy remained high (100%) for all values from K = 1 to 9.
- Slight performance drop at K=10 on some random seeds.

### 🧠 Decision Boundary
- A 2D plot (using PetalLengthCm and PetalWidthCm) showed clear, non-overlapping regions for each species.
- KNN performed well due to the well-separated classes.

## 📌 Inference
- KNN is highly effective for the Iris dataset due to distinct class separation.
- Normalization played a key role in accurate distance measurement.
- A low value of K (3) gave perfect classification, indicating that class boundaries are crisp.  