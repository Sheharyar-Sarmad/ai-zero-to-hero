

# Evaluation of Model

- Model Evaluation is the process of measuring how well a trained machine learning model performs on unseen data.
- In classification, models are commonly evaluated using the **Confusion Matrix**, **Accuracy**, **Precision**, **Recall**, **F1-Score**, **ROC-AUC**, and **Log Loss**.
- The goal of model evaluation is to assess the model's prediction performance and determine whether it generalizes well to real-world data.

# Confusion Matrix

- A **Confusion Matrix** is an evaluation tool used to measure the performance of a **binary classification** model.
- It compares the **actual labels** with the **predicted labels** and summarizes the results in a matrix.
- The confusion matrix consists of four outcomes:
  - **True Positive (TP)**
  - **True Negative (TN)**
  - **False Positive (FP)**
  - **False Negative (FN)**
  - The confusion comes from thinking the **1s and 0s** on the **top and lef**t are being compared to each other. They are not. Instead, each prediction for each sample is placed into one of the four boxes.

| Person | Actual | Predicted |       Value        |
| ------ | ------ | --------- | ------------------ |
| A      | 1      | 1         | TP(true positive)  |
| B      | 1      | 0         | FN(false negative) |
| C      | 0      | 1         | FP(false positive) |
| D      | 0      | 0         | TF(false negative) |

- For each data sample, first look at the **Actual** value, then look at the **Predicted** value.
- The **Actual** value chooses the **row**, and the **Predicted** value chooses the **column**.
- The box where that row and column meet tells whether the prediction is **TP, TN, FP, or FN**.

> Type I Error (False Positive)

- A Type I Error occurs when the model predicts Positive (1), but the actual class is Negative (0).

> Type II Error (False Negative)

- A Type II Error occurs when the model predicts Negative (0), but the actual class is Positive (1).

- Using these four values, we can calculate important evaluation metrics such as **Accuracy**, **Precision**, **Recall**, and **F1-Score**.

# Accuracy:

- **Accuracy** is the percentage of predictions that the model made correctly out of all predictions.
- **Accuracy** = **Correct Predictions ÷ Total Predictions**

-  **Accuracy** = **(TP + TN) / (TP + TN + FP + FN)**
-  **Example**  = 190 + 40 / 190 + 10 + 10 + 40
-               = 230 / 250
-               = **0.92** -- that means your model is 0.92 * 100 = 92% accurate and its very perfect model.

# Precision:

- **Precision** tells us how many of the predicted positive cases are actually positive.
- **Precision** = Correct Positive Predictions ÷ Total Positive Predictions

- **Precsion** = **TP / TP + FP**
- **Example**  = 190 / 190 + 10
-              = 0.95 -- that means 0.95 * 100 = 95% of the prediction made by the model is correct

# Recall:

- **Recall** tells us out of all actual **positive**, how many we **correctly predicted positive**. Use it when **FN** is costly(disease detection).
- **Recall** = **Correct Positive Predictions ÷ Total Actual Positives**

- **Recall**  = **TP / TP +FN**
- **Example** = 190 / 190 + 10
-             = 0.95 -- that means 0.95 × 100 = 95% of all actual positive cases were correctly identified by the model.

# F1 Score:

- **F1 Score** is a metric that combines **Precision** and **Recall** into a **single value**. It is used when you want a **balance** between these **two metrics**, especially for **imbalanced datasets**. Its **Harmonic Mean of Precision and Recall**. This is used when you want balance between **Precision and Recall**.
- **F1 Score** = **2 × (Precision × Recall) ÷ (Precision + Recall)**

- **F1 Score** = **2 . TP / (2 . TP + FP + FN)**
