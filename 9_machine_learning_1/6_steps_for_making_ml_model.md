# Steps in Making a Machine Learning Model

## 1 - Problem Definition
- Understand the business goal
- Define what you want to predict (target variable)
- Determine problem type: Classification, Regression, or Clustering
- Set success metrics (accuracy, precision, etc.)

---

## 2 - Data Collection
- Gather data from multiple sources (databases, APIs, CSV, web scraping)
- Ensure data is relevant to the problem
- Collect sufficient quantity and quality of data

---

## 3 - Exploratory Data Analysis (EDA)
- Understand data structure and distributions
- Find patterns, trends, and relationships
- Visualize data using plots (histograms, scatter plots, heatmaps)
- Identify correlations between features and target

---

## 4 - Data Preprocessing / Cleaning
- Handle missing values (fill or drop)
- Remove duplicates
- Detect and treat outliers
- Encode categorical variables (One-Hot, Label Encoding)
- Scale/Normalize numerical features
- Convert data into proper format

---

## 5 - Feature Selection & Engineering
- Select most relevant features for the model
- Remove redundant or irrelevant features
- Create new features from existing ones (ratios, aggregates, date parts)
- Transform features (log, square root, binning)
- Reduce dimensionality if needed

---

## 6 - Split the Dataset
- Divide data into Training, Validation, and Test sets
- Typical split: 70-80% training, 10-15% validation, 10-15% test
- Use stratification for classification (maintain class balance)
- Keep test data untouched until final evaluation

---

## 7 - Model Selection
- Choose appropriate algorithm based on problem type
- Start with simple baselines (Linear Regression, Logistic Regression, Decision Trees)
- Experiment with advanced models (Random Forest, XGBoost, Neural Networks)
- Consider trade-offs: accuracy vs interpretability vs speed

---

## 8 - Model Training
- Train model on training dataset
- Model learns patterns from the data
- Monitor for overfitting (high training accuracy, low validation accuracy)
- Use validation set to check performance during training

---

## 9 - Model Evaluation
- Evaluate model on validation set using appropriate metrics
- Classification: Accuracy, Precision, Recall, F1, ROC-AUC
- Regression: MAE, MSE, RMSE, R²
- Analyze confusion matrix and error patterns
- Compare with baseline performance

---

## 10 - Hyperparameter Tuning
- Optimize model parameters that are not learned from data
- Use Grid Search (exhaustive) or Random Search (efficient)
- Advanced: Bayesian Optimization (Optuna, Hyperopt)
- Use cross-validation during tuning for reliable results
- Select best parameter combination

---

## 11 - Model Testing / Validation
- Finally evaluate on unseen Test set
- This gives true generalization performance
- Ensure no data leakage from test set during training
- Validate model meets business requirements
- Document final performance metrics

---

## Summary Flow
> Problem → Data → EDA → Clean → Features → Split → Select → Train → Evaluate → Tune → Test

> **Key Rule:** Only touch the Test set ONCE — at the very end!