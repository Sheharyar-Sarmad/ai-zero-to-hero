# Introduction to Linear Algebra

## What is Linear Algebra?

Linear Algebra is a branch of mathematics that deals with:

- Vectors
- Matrices
- Linear equations
- Linear transformations
- Vector spaces

It is one of the most important mathematical foundations of
Data Science, Machine Learning, and Artificial Intelligence.

---

## Usage of Linear Algebra

Linear Algebra is used in many fields such as:

- Computer Science
- Physics
- Electrical Engineering
- Mechanical Engineering
- Statistics
- Data Science
- Machine Learning
- Artificial Intelligence
- Computer Graphics
- Robotics

---

# Numeric vs Geometric Level

Linear Algebra can be understood at two different levels.

## 1. Numeric Level

At the numeric level, we work with:

- Numbers
- Equations
- Vectors
- Matrices

Example:

```text
2x + 3y = 10

We solve problems using mathematical calculations.

2. Geometric Level

At the geometric level, we visualize mathematical objects.

For example:

[3]
[2]

can represent a point:

(3, 2)

or a vector that moves:

3 units horizontally
2 units vertically

The numeric level focuses on calculations.

The geometric level focuses on visualization.

Scalars

A scalar is a single number.

Examples:

5
-3
0
2.5

Scalars represent quantities such as:

Temperature
Speed
Time
Mass

A scalar can multiply a vector.

Example:

3 × [2, 4] = [6, 12]
Vectors

A vector is an ordered collection of numbers.

Example:

v = [2, 4]

This is a two-dimensional vector.

A vector can represent:

Direction
Magnitude
Position
Features of data

In Machine Learning, a data point is often represented as a vector.

Example:

[Age, Salary, Experience]
Vector Components

The individual values inside a vector are called components.

Example:

v = [3, 5]

Here:

x-component = 3
y-component = 5

The number of components determines the dimension of a vector.

Vector Addition

Vectors are added component by component.

Example:

u = [2, 3]
v = [4, 5]
u + v = [2 + 4, 3 + 5]
u + v = [6, 8]
Vector Subtraction

Vectors can also be subtracted component by component.

u = [5, 7]
v = [2, 3]
u - v = [5 - 2, 7 - 3]
u - v = [3, 4]
Scalar Multiplication

A vector can be multiplied by a scalar.

v = [2, 3]
3v = 3[2, 3]
3v = [6, 9]

Scalar multiplication changes the size of a vector.

A negative scalar can also reverse its direction.

Magnitude of a Vector

The magnitude is the length of a vector.

For a 2D vector:

v = [x, y]

The formula is:

||v|| = √(x² + y²)

Example:

v = [3, 4]
||v|| = √(3² + 4²)
||v|| = √25 = 5
Dot Product

The dot product is an operation between two vectors.

For:

u = [u1, u2]
v = [v1, v2]

The formula is:

u · v = u1v1 + u2v2

Example:

u = [2, 3]
v = [4, 5]
u · v = (2 × 4) + (3 × 5)
u · v = 23

The result of a dot product is a scalar.

Matrices

A matrix is a rectangular arrangement of numbers.

Example:

A =
[1  2]
[3  4]

This matrix has:

2 rows
2 columns

Therefore, its shape is:

2 × 2
Matrices in Data Science

A dataset can be represented as a matrix.

Example:

Age  Experience  Salary

20       1        50000
25       3        70000
30       5        90000

Each row represents:

One observation

Each column represents:

One feature
Linear Equations

Linear Algebra is used to solve systems of linear equations.

Example:

2x + y = 5
x + y = 3

These equations can be represented using matrices.

The general form is:

AX = B

Where:

A = Coefficient Matrix
X = Variable Vector
B = Constant Vector
Linear Algebra in Machine Learning

Machine Learning uses vectors and matrices to represent data.

For example:

X = [Age, Salary, Experience]

A model can use these features to make predictions.

A simple prediction equation is:

y = wᵀx + b

Here:

x = Input Features
w = Weights
b = Bias
y = Prediction

This is a direct application of Linear Algebra.

Linear Algebra in Neural Networks

Neural Networks use many mathematical operations.

The most important operations include:

Vector multiplication
Matrix multiplication
Dot products
Addition

A neuron can be represented as:

z = wᵀx + b

Deep Learning models perform millions or billions of
matrix operations.

Therefore, Linear Algebra is an important foundation
for Machine Learning and Artificial Intelligence.

Summary

Linear Algebra is used to study:

Scalars
Vectors
Matrices
Linear equations
Vector operations

Numeric level focuses on calculations.

Geometric level focuses on visualization.

The most important concepts for Machine Learning are:

Vectors
Matrices
Dot Product
Matrix Multiplication
Linear Equations

Linear Algebra is one of the core mathematical foundations of:

Data Science
Machine Learning
Deep Learning
Artificial Intelligence