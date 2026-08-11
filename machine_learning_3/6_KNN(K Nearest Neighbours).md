
K-Nearest Neighbors (KNN)

1. What is KNN?

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm that makes predictions by looking at the most similar datapoints in the training dataset.

KNN is commonly used for:

Classification

Regression

KNN is called a lazy learning algorithm because it does not learn anexplicit mathematical model during training. Instead, it stores the training data and performs the main computation when making a prediction.

2. Core Idea

The basic idea is:

A data point is likely to have a similar output to the data points closest to it.

For classification:

Choose a value of K.

Calculate the distance between the new input and training points.

Find the K nearest points.

Look at their classes.

Assign the class with the majority vote.

Example:

New point
   ↓
Find nearest K points
   ↓
Majority vote
   ↓
Predicted class

3. KNN and N-Dimensional Vectors

A data point can be represented as an N-dimensional vector.

For example, with 2 features:

X = [x₁, x₂]

This is a 2-dimensional vector.

With 3 features:

X = [x₁, x₂, x₃]

This is a 3-dimensional vector.

With N features:

X = [x₁, x₂, ..., xₙ]

So, in KNN:

Each observation/data point can be represented as an N-dimensional vector.

Example:

Age     Salary     Experience
25      50000      2
30      70000      5

Each row is a vector:

[25, 50000, 2]
[30, 70000, 5]

Therefore, KNN works by measuring the distance between these vectors.

4. Euclidean Distance

One of the most commonly used distance metrics in KNN is Euclidean distance.

For two points:

A = [x₁, x₂]
B = [y₁, y₂]

the Euclidean distance is:

$$d(A,B) = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2}$$

For N dimensions:

$$d(A,B) =\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$

In simple terms:

Euclidean distance measures how far two vectors/data points are from each other.

5. Example of Euclidean Distance

Suppose:

A = [2, 3]
B = [5, 7]

Then:

\sqrt{(2-5)^2+(3-7)^2}$$

$$\sqrt{9+16}$$

$$\sqrt{25}$$$$=5$$

So the distance between A and B is:

5

A smaller distance means the points are more similar according to the selected distance metric.

6. Input to KNN

The input to KNN consists of:

Training data

X_train

The feature vectors used to find neighbors.

Target values

y_train

The corresponding class labels for classification or numerical valuesfor regression.

New input

X_new

The new data point for which we want a prediction.

K value

K

The number of nearest neighbors to consider.

Conceptually:

X_train + y_train
        ↓
   KNN algorithm
        ↑
      X_new
        +
        K
        ↓
   Prediction

7. What is K?

K represents the number of nearest neighbors that KNN considers when making a prediction.

For example:

K = 3

means:

Look at the 3 closest data points.

If:

K = 5

then:

Look at the 5 closest data points.

8. Choosing K

Choosing K is important.

Small K

Example:

K = 1

The model considers only the closest point.

Advantages:

Very sensitive to local patterns.

Disadvantages:

Can be sensitive to noise.

Can overfit.

Large K

Example:

K = 50

The prediction considers many points.

Advantages:

Less sensitive to individual noisy observations.

Disadvantages:

Can become too generalized.

Can underfit.

Therefore:

K should be selected experimentally rather than randomly.

9. KNN Classification

Suppose:

K = 5

The five nearest neighbors have:

Class A
Class A
Class B
Class A
Class B

Count:

Class A → 3
Class B → 2

Therefore:

Prediction = Class A

This is called majority voting.

10. KNN Regression

KNN can also be used for regression.

Instead of voting for a class, the algorithm can use the values of the nearest neighbors.

Example:

K = 3

Neighbor values:
10
12
14

A simple KNN regression prediction is:

$$\frac{10+12+14}{3}=12$$

Therefore:

Prediction = 12

11. Why Feature Scaling is Important

KNN is a distance-based algorithm.

Therefore, feature scales can strongly affect the distance calculation.

Suppose:

Age = 20
Salary = 100000

Salary has a much larger numerical scale than age.

Without scaling, salary can dominate the Euclidean distance.

Therefore, KNN commonly benefits from:

Standardization

Min-Max scaling

Example standardization:

$$z = \frac{x-\mu}{\sigma}$$

In scikit-learn:

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

Important:

Fit the scaler on training data and transform both training and testdata using that fitted scaler.

12. KNN Experiment

A good KNN workflow is to experiment with different values of K.

For example:

K = 1
K = 3
K = 5
K = 7
K = 9
...

For every K:

Train/use KNN with that K.

Evaluate the model.

Record the score.

Compare the results.

Example:

 K   Accuracy

 1        78%
 3        82%
 5        85%
 7        87%
 9        86%
11        84%

Here:

Best observed K = 7

because it produced the highest validation accuracy.

13. Cross-Validation for Choosing K

Instead of relying on only one train/test split, we can usecross-validation.

For example:

5-Fold Cross-Validation

The training data is divided into 5 folds.

Conceptually:

Fold 1 → Validation
Fold 2 → Validation
Fold 3 → Validation
Fold 4 → Validation
Fold 5 → Validation

Each fold gets a chance to act as the validation set.

Then calculate the average score.

Example:

 K   Mean CV Accuracy

 1              79.2%
 3              83.8%
 5              86.1%
 7              87.4%
 9              86.8%
11              85.3%

Here:

Best K = 7

because it has the highest mean cross-validation score.

14. KNN with Cross-Validation in Scikit-Learn

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

k_values = range(1, 16)

results = {}

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)

    scores = cross_val_score(
        model,
        X_train_scaled,
        y_train,
        cv=5,
        scoring="accuracy"
    )

    results[k] = scores.mean()

best_k = max(results, key=results.get)

print("Best K:", best_k)
print("Best CV Accuracy:", results[best_k])

Then create the final model:

knn = KNeighborsClassifier(n_neighbors=best_k)

knn.fit(X_train_scaled, y_train)

And evaluate on the test set:

test_accuracy = knn.score(X_test_scaled, y_test)

print("Test Accuracy:", test_accuracy)

15. KNN is Not Limited to Classification

KNN is often introduced as a classification algorithm, but technically it can be used for both:

KNN
├── Classification
└── Regression

Classification:

from sklearn.neighbors import KNeighborsClassifier

Regression:

from sklearn.neighbors import KNeighborsRegressor

16. When to Use KNN Instead of Another Classification Algorithm

KNN can be useful when:

The dataset is relatively small or moderate.

Similar observations tend to have similar labels.

The decision boundary may be nonlinear.

You want a simple baseline model.

You don't want to assume a particular functional form for the decision boundary.

The features have meaningful distance relationships.

Example:

Customer A → similar age, income, behavior
Customer B → similar age, income, behavior
Customer C → very different characteristics

If similar customers tend to have the same target class, KNN can workwell.

17. When KNN May Not Be a Good Choice

KNN can struggle when:

Very large datasets

Prediction requires finding nearby training points, which can become computationally expensive.

High-dimensional data

As the number of dimensions increases, distance-based methods can become less effective.

This is related to the:

Curse of Dimensionality

Poorly scaled features

A large-scale feature can dominate the distance.

Irrelevant features

Unimportant features can distort distances.

Sparse/high-dimensional data

Distance relationships may become less useful.

18. KNN as a Baseline / Experiment

KNN is often useful as an experimental baseline.

For example, when solving a classification problem:

Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Feature Scaling
   ↓
KNN
   ↓
Experiment with K
   ↓
Cross-Validation
   ↓
Evaluate

Then compare it against other models:

KNN
Logistic Regression
Decision Tree
Random Forest
SVM
Gradient Boosting

You don't necessarily choose KNN simply because it has a good score.

You compare:

Accuracy

Precision

Recall

F1-score

Confusion matrix

Cross-validation performance

Prediction speed

Interpretability

Dataset size

Computational cost

19. Important KNN Parameters in Scikit-Learn

KNeighborsClassifier(
    n_neighbors=5,
    weights="uniform",
    metric="minkowski",
    p=2
)

n_neighbors

Controls K:

n_neighbors=5

means:

K = 5

weights

Default:

weights="uniform"

Every neighbor has equal voting weight.

Another option:

weights="distance"

Closer neighbors receive more influence.

metric

Controls how distance is calculated.

p

For Minkowski distance:

p = 2 → Euclidean distance
p = 1 → Manhattan distance

20. Complete KNN Workflow

             Dataset
                ↓
          Clean the data
                ↓
        Separate X and y
                ↓
        Train/Test Split
                ↓
        Feature Scaling
                ↓
       Experiment with K
                ↓
        Cross-Validation
                ↓
          Select Best K
                ↓
       Train Final KNN
                ↓
       Test Set Evaluation
                ↓
       Compare with other
       classification models

21. Key Formulas

Euclidean Distance

For N-dimensional vectors:

\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$

KNN Classification

Prediction = Majority class among K nearest neighbors

Simple KNN Regression

\frac{1}{K}\sum_{i=1}^{K} y_i$$

22. Quick Revision

KNN
│
├── Supervised Learning
│
├── Classification
│
├── Regression
│
├── Input → N-dimensional feature vector
│
├── Calculate distance
│
├── Euclidean distance is commonly used
│
├── Find K nearest neighbors
│
├── Classification → Majority voting
│
├── Regression → Neighbor values
│
├── K is a hyperparameter
│
├── Small K → Can overfit
│
├── Large K → Can underfit
│
├── Feature scaling is important
│
├── Experiment with different K values
│
├── Cross-validation helps select K
│
└── Compare KNN with other models

23. One-Line Definition

K-Nearest Neighbors (KNN) is a supervised, distance-based algorithm that predicts a new data point using the outputs of its K nearest training examples.