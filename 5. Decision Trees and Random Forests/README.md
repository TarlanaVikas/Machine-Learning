# Decision Trees and Random Forests



## Objective



Learn and implement tree-based machine learning models, including **Decision Tree** and **Random Forest**, for classification tasks using the Heart Disease dataset.



## Folder Structure



```text

decision_trees/

|

|-- heart.csv

|-- main.py

|-- README.md

`-- observations.md

```



## Tools Used



* Python

* Pandas

* Matplotlib

* Seaborn

* Scikit-learn

* Graphviz (optional, for advanced tree visualizations)



## Installation



Activate your virtual environment and install the required libraries:



```bash

pip install pandas scikit-learn matplotlib seaborn graphviz

```



## Steps Performed



* Created the project folder `task_5_decision_trees` and placed `heart.csv` inside it.

* Created a `main.py` file and implemented the project step by step.

* Imported the required libraries for EDA, model building, visualization, and evaluation.

* Loaded the Heart Disease dataset using Pandas.

* Split the dataset into training and testing sets using an 80/20 split.

* Trained a Decision Tree Classifier with `max_depth=4`.

* Visualized the Decision Tree using `plot_tree()`.

* Evaluated the Decision Tree using accuracy, confusion matrix, and classification report.

* Trained a Random Forest Classifier with 100 trees.

* Compared the performance of the Decision Tree and Random Forest models.

* Plotted feature importances for the Random Forest model.

* Performed 5-fold cross-validation to evaluate model reliability across different folds.



## Output Highlights



1. Decision Tree and Random Forest classifiers were trained and evaluated.

2. Accuracy scores and classification metrics were compared.

3. Important features affecting the prediction were visualized.

4. Cross-validation was performed to check the consistency of model performance.



## How to Run



Run the following command from the project directory:



```bash

python main.py

```



The program will:



* Load and process the Heart Disease dataset.

* Train the Decision Tree classifier.

* Train the Random Forest classifier.

* Print evaluation metrics.

* Display the Decision Tree visualization.

* Display the Random Forest feature importance plot.

* Perform cross-validation and display the results.


# Observations : Decision Trees & Random Forests

## Dataset Overview
* **Dataset**: Heart Disease Prediction
* **Rows**: 1025
* **Columns**: 14
* **Target Variable**: `target` (Binary – 0: No disease, 1: Disease)

---

## Model 1: Decision Tree

### Configuration
* `max_depth = 4`

### Evaluation
* **Accuracy**: ~0.80
* **Confusion Matrix** showed a reasonable balance of true positives and negatives.
* Good for interpretability but can overfit if not pruned or controlled.

---

## Model 2: Random Forest

### Configuration
* `n_estimators = 100` (number of trees)

### Evaluation
* **Accuracy**: Slightly higher than Decision Tree (~0.83)
* **Better generalization** due to ensembling.
* **Feature importance plot** revealed key predictors like:
  - `cp` (chest pain type)
  - `thalach` (max heart rate)
  - `exang` (exercise-induced angina)

---

## Feature Importance (Top 5)

| Feature        | Importance |
|----------------|------------|
| `cp`           | High       |
| `thalach`      | High       |
| `exang`        | Moderate   |
| `oldpeak`      | Moderate   |
| `slope`        | Moderate   |

---

## Cross-Validation

* 5-fold cross-validation showed consistent performance.
* Mean CV accuracy: ~0.82

---

## Summary

* **Decision Trees** offer transparency and are easy to interpret.
* **Random Forests** provide higher accuracy and stability.
* **Chest pain type, heart rate, and angina** are significant indicators of heart disease.
