# Covariance and Correlation

## Introduction

In statistics, we often work with more than one variable.

For example:

- Hours studied
- Exam marks

We may want to understand:

> Is there a relationship between hours studied and exam marks?

For example, if a student studies more hours, do their marks also increase?

To study the relationship between two variables, we use:

1. Covariance
2. Correlation

Both covariance and correlation help us understand how two variables change together.

---

# What is a Variable?

A variable is a characteristic or quantity that can change.

Examples:

- Age
- Height
- Weight
- Salary
- Temperature
- Study hours
- Exam marks
- Experience

Suppose:

```text
X = Hours Studied

Y = Exam Marks

We can investigate whether changes in X are related to changes in Y.

Relationship Between Two Variables

Suppose we have the following data:

Hours Studied	Exam Marks
1	20
2	30
3	40
4	50
5	60

As the number of study hours increases, exam marks also increase.

This indicates a positive relationship.

The two most common statistical measurements for studying this relationship are:

Covariance
Correlation
Covariance
Definition

Covariance measures the direction in which two variables change together.

It tells us whether:

Both variables increase together
One variable increases while the other decreases
There is no clear linear relationship

Covariance focuses mainly on the direction of the relationship.

How Covariance Works

Suppose we have two variables:

X = Study Hours

Y = Exam Marks

If:

X increases
Y also increases

Then the covariance is positive.

If:

X increases
Y decreases

Then the covariance is negative.

If there is no clear pattern, the covariance may be close to zero.

Types of Covariance
Positive Covariance

Positive covariance occurs when two variables generally move in the same direction.

Example:

Study Hours ↑
Exam Marks ↑

Mathematically:

Cov(X, Y) > 0

Example:

Study Hours	Marks
1	20
2	30
3	40
4	50
5	60

As study hours increase, marks also increase.

Therefore, the covariance is positive.

Negative Covariance

Negative covariance occurs when two variables generally move in opposite directions.

Example:

Price ↑
Demand ↓

Mathematically:

Cov(X, Y) < 0

Example:

Price	Demand
10	90
20	80
30	70
40	60
50	50

As price increases, demand decreases.

Therefore, the covariance is negative.

Zero Covariance

If two variables do not have a clear linear relationship, their covariance may be close to zero.

Cov(X, Y) ≈ 0

This means that the variables do not show a clear linear pattern.

Important:

Covariance = 0

does not necessarily mean that there is absolutely no relationship.

There may still be a nonlinear relationship.

Covariance Formula
Population Covariance

The population covariance formula is:

Cov(X, Y) = Σ[(X - μx)(Y - μy)] / N

Where:

X = Individual values of variable X

Y = Individual values of variable Y

μx = Population mean of X

μy = Population mean of Y

N = Total number of observations
Sample Covariance

When working with a sample, we use:

Cov(X, Y) = Σ[(X - x̄)(Y - ȳ)] / (n - 1)

Where:

x̄ = Sample mean of X

ȳ = Sample mean of Y

n = Number of observations

The denominator is:

n - 1

because we are calculating covariance from a sample.

Manual Covariance Example

Suppose:

X = [1, 2, 3]
Y = [2, 4, 6]
Step 1: Calculate the Mean of X
Mean of X = (1 + 2 + 3) / 3
Mean of X = 2

Therefore:

x̄ = 2
Step 2: Calculate the Mean of Y
Mean of Y = (2 + 4 + 6) / 3
Mean of Y = 4

Therefore:

ȳ = 4
Step 3: Calculate Deviations
X	Y	X - x̄	Y - ȳ
1	2	-1	-2
2	4	0	0
3	6	1	2
Step 4: Multiply the Deviations
X - x̄	Y - ȳ	Product
-1	-2	2
0	0	0
1	2	2

Sum of products:

2 + 0 + 2 = 4
Step 5: Calculate Population Covariance
Cov(X, Y) = 4 / 3
Cov(X, Y) = 1.33

The covariance is positive.

This tells us:

When X increases, Y also tends to increase.
Important Limitation of Covariance

The main problem with covariance is that its value depends on the units of the variables.

For example, suppose we measure height in:

Centimeters

Then we get one covariance value.

If we convert height to:

Meters

The covariance value changes.

Therefore, covariance does not have a fixed range.

It can be:

-∞ to +∞

This makes covariance difficult to interpret.

For example:

Covariance = 100

Is this a strong relationship?

Or is it a weak relationship?

It is difficult to tell.

This is where correlation becomes useful.

Correlation
Definition

Correlation measures both:

The direction of a relationship
The strength of a relationship

between two variables.

Correlation is a standardized form of covariance.

The most commonly used correlation coefficient is:

Pearson Correlation Coefficient

It is represented by:

r
Range of Correlation

The correlation coefficient always lies between:

-1 and +1

Mathematically:

-1 ≤ r ≤ +1

This makes correlation easy to interpret.

Meaning of Correlation Values
r = +1

This represents a perfect positive correlation.

X increases
Y also increases

All points lie perfectly on an upward-sloping straight line.

Example:

X = [1, 2, 3, 4, 5]

Y = [2, 4, 6, 8, 10]
r = -1

This represents a perfect negative correlation.

X increases
Y decreases

All points lie perfectly on a downward-sloping straight line.

Example:

X = [1, 2, 3, 4, 5]

Y = [10, 8, 6, 4, 2]
r = 0

This indicates no linear correlation.

r = 0

There is no clear linear relationship between the variables.

Important:

A correlation of zero does not always mean there is absolutely no relationship.

The variables may have a nonlinear relationship.

Positive Correlation

A positive correlation occurs when both variables tend to move in the same direction.

Example:

Exercise Time ↑
Fitness Level ↑

Another example:

Experience ↑
Salary ↑

Positive correlation:

0 < r ≤ 1

Example:

r = 0.85

This represents a strong positive relationship.

Negative Correlation

A negative correlation occurs when variables move in opposite directions.

Example:

Price ↑
Demand ↓

Another example:

Speed ↑
Travel Time ↓

Negative correlation:

-1 ≤ r < 0

Example:

r = -0.85

This represents a strong negative relationship.

Strength of Correlation

The absolute value of the correlation coefficient tells us the strength.

The closer the value is to:

+1 or -1

the stronger the relationship.

The closer the value is to:

0

the weaker the linear relationship.

General Interpretation
Correlation Value	Interpretation
0.00	No linear correlation
±0.01 to ±0.19	Very weak
±0.20 to ±0.39	Weak
±0.40 to ±0.59	Moderate
±0.60 to ±0.79	Strong
±0.80 to ±0.99	Very strong
±1.00	Perfect

These ranges are general guidelines.

Different fields may use slightly different interpretations.

Pearson Correlation Coefficient

The Pearson correlation coefficient is calculated using:

r = Cov(X, Y) / (σx × σy)

Where:

Cov(X, Y) = Covariance between X and Y

σx = Standard deviation of X

σy = Standard deviation of Y

This formula converts covariance into a standardized value.

That is why the result always falls between:

-1 and +1
Another Formula for Pearson Correlation

The formula can also be written as:

r =
Σ[(X - x̄)(Y - ȳ)]
/
√[Σ(X - x̄)^2 × Σ(Y - ȳ)^2]

This formula compares:

The joint variation of X and Y

with:

The individual variation of X and Y
Relationship Between Covariance and Correlation

Correlation is essentially standardized covariance.

Correlation =
Covariance
/
(Standard Deviation of X × Standard Deviation of Y)

Therefore:

Covariance tells us the direction.
Correlation tells us the direction and strength.
Covariance vs Correlation
Feature	Covariance	Correlation
Measures direction	Yes	Yes
Measures strength	Difficult	Yes
Range	No fixed range	-1 to +1
Depends on units	Yes	No
Standardized	No	Yes
Easy to interpret	Less easy	Easier
Used in machine learning	Yes	Yes
Example Comparing Covariance and Correlation

Suppose:

X = Study Hours

Y = Exam Marks

If students who study more generally get higher marks:

Cov(X, Y) > 0

This tells us that the relationship is positive.

If:

r = 0.90

we can say:

There is a very strong positive linear relationship
between study hours and exam marks.

Correlation gives us more information than covariance because it tells us how strong the relationship is.

Correlation Does Not Mean Causation

This is one of the most important concepts in statistics.

Correlation ≠ Causation

If two variables are correlated, it does not automatically mean that one variable causes the other.

Example of Correlation Without Direct Causation

Suppose we observe:

Ice Cream Sales ↑
Drowning Cases ↑

These two variables may have a positive correlation.

However, this does not mean:

Ice Cream causes drowning.

A third variable may influence both:

Hot Weather

During hot weather:

Ice Cream Sales increase.

At the same time:

More people swim.

This can lead to:

More drowning cases.

Therefore:

Hot Weather

is a possible confounding variable.

Spurious Correlation

A spurious correlation occurs when two variables appear to be related, but the relationship may be coincidental or caused by another variable.

Example:

Variable A ↑
Variable B ↑

This does not automatically prove:

A causes B

To establish causation, we need more evidence.

Correlation only tells us that variables move together.

Linear Correlation

Correlation usually measures the strength of a linear relationship.

A linear relationship follows a pattern similar to:

Y = aX + b

When X increases, Y changes at a relatively consistent rate.

Example:

X: 1, 2, 3, 4, 5
Y: 2, 4, 6, 8, 10

This is a perfect positive linear relationship.

Nonlinear Relationship

Two variables may have a strong relationship but have a correlation close to zero if the relationship is nonlinear.

Example:

Y = X²

The relationship exists, but it is curved rather than a straight line.

Therefore:

Correlation mainly measures linear relationships.

This is important when interpreting correlation.

Scatter Plot

A scatter plot is commonly used to visualize the relationship between two numerical variables.

Example:

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)

plt.xlabel("X")
plt.ylabel("Y")

plt.show()

If the points move upward from left to right:

Positive correlation

If the points move downward from left to right:

Negative correlation

If the points are randomly scattered:

Weak or no linear correlation
Correlation Using NumPy
import numpy as np

x = [1, 2, 3, 4, 5]

y = [2, 4, 6, 8, 10]

correlation_matrix = np.corrcoef(x, y)

print(correlation_matrix)

The output is a correlation matrix:

[[1. 1.]
 [1. 1.]]

The diagonal values are always:

1

because every variable has a perfect correlation with itself.

The other values show the correlation between X and Y.

Covariance Using NumPy
import numpy as np

x = [1, 2, 3, 4, 5]

y = [2, 4, 6, 8, 10]

covariance_matrix = np.cov(x, y)

print(covariance_matrix)

The result is a covariance matrix:

[
    [Cov(X, X), Cov(X, Y)],
    [Cov(Y, X), Cov(Y, Y)]
]

The diagonal values represent variance:

Cov(X, X) = Variance of X

Cov(Y, Y) = Variance of Y

The off-diagonal values represent covariance:

Cov(X, Y)

Cov(Y, X)
Correlation Using Pandas
import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

print(df.corr())

Output:

              Study_Hours  Marks
Study_Hours           1.0    1.0
Marks                 1.0    1.0

This indicates a perfect positive correlation.

Covariance Using Pandas
print(df.cov())

This calculates the covariance between all numerical columns.

Correlation Matrix

When a dataset contains many numerical variables, we can calculate a correlation matrix.

Example:

             Age  Salary  Experience
Age          1.00   0.75       0.80
Salary       0.75   1.00       0.90
Experience   0.80   0.90       1.00

The diagonal is always:

1.00

because each variable has a perfect correlation with itself.

Correlation Heatmap

A heatmap provides a visual representation of correlations.

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(
    df.corr(),
    annot=True
)

plt.show()

The correlation heatmap helps us quickly identify:

Strong positive relationships
Strong negative relationships
Weak relationships
Possible relationships between features
Correlation in Machine Learning

Correlation is very important in machine learning.

Suppose we have the following features:

Age
Salary
Experience
Education

We can calculate the correlation between features.

If two features have very high correlation:

Correlation ≈ 1

they may contain similar information.

This can sometimes cause a problem called:

Multicollinearity
Multicollinearity

Multicollinearity occurs when independent variables are highly correlated with each other.

Example:

Years of Experience

and:

Age

may be strongly correlated.

If multiple features provide almost the same information, some machine learning models may have difficulty determining the individual effect of each feature.

Correlation and Feature Selection

Correlation can help us select useful features.

For example, suppose we want to predict:

House Price

Features:

House Size
Number of Rooms
Distance from City
Age of House

We can calculate their correlations with house price.

A feature with a strong relationship may be useful for prediction.

However:

Correlation alone does not determine whether a feature should be used.

We must also consider:

Domain knowledge
Data quality
Nonlinear relationships
Missing values
Multicollinearity
Important Difference Between Correlation and Regression

Correlation measures:

The strength and direction of a relationship.

Regression is used to:

Predict one variable using another variable or multiple variables.

Example:

Correlation:
Are study hours and marks related?
Regression:
Can we predict marks based on study hours?

Correlation and regression are related, but they are not the same thing.

Covariance and Correlation Summary
Covariance

Covariance measures the direction in which two variables change together.

Positive Covariance:
Both variables tend to increase together.
Negative Covariance:
One variable tends to increase while the other decreases.
Zero Covariance:
No clear linear relationship.

Covariance has no fixed range:

-∞ to +∞
Correlation

Correlation measures:

Direction

and:

Strength

of a linear relationship.

Its range is:

-1 to +1
Important Formulas
Population Covariance
Cov(X, Y) = Σ[(X - μx)(Y - μy)] / N
Sample Covariance
Cov(X, Y) = Σ[(X - x̄)(Y - ȳ)] / (n - 1)
Pearson Correlation
r = Cov(X, Y) / (σx × σy)
Final Key Points
Covariance measures the direction of the relationship between two variables.
Correlation measures both the direction and strength of the relationship.
Positive covariance means variables tend to move in the same direction.
Negative covariance means variables tend to move in opposite directions.
Correlation always lies between -1 and +1.
A correlation close to +1 indicates a strong positive relationship.
A correlation close to -1 indicates a strong negative relationship.
A correlation close to 0 indicates a weak or no linear relationship.
Correlation does not prove causation.
Correlation mainly measures linear relationships.
Covariance depends on the units of measurement.
Correlation is standardized and therefore easier to interpret.
Easy Way to Remember
Covariance = Direction
Correlation = Direction + Strength

And remember:

Correlation ≠ Causation

This is now a **single complete long `.md` file** for both topics.