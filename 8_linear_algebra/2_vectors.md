Vectors in Linear Algebra
What is a Vector?

A vector is an ordered collection of numbers.

Example:

v = [2, 3]

A vector can represent:

A point
A direction
A magnitude
Movement
Features of a dataset

Vectors are one of the most important concepts in Linear Algebra.

Scalars vs Vectors
Scalar

A scalar is a single number.

Examples:

5
-2
0
3.14

A scalar has only:

Magnitude

Example:

Temperature = 30°C
Vector

A vector contains multiple values.

Example:

v = [3, 4]

A vector can have:

Magnitude + Direction
Vector Notation

A vector can be written in different ways.

Row Vector
v = [2, 3, 4]
Column Vector
v =
[2]
[3]
[4]

Both represent the same vector.

Components of a Vector

The individual values inside a vector are called components.

Example:

v = [5, 7, 2]

The components are:

v1 = 5
v2 = 7
v3 = 2
Dimension of a Vector

The number of components determines the dimension of a vector.

One-Dimensional Vector
v = [5]

Dimension:

1
Two-Dimensional Vector
v = [3, 4]

Dimension:

2
Three-Dimensional Vector
v = [1, 2, 3]

Dimension:

3
n-Dimensional Vector

A vector can have any number of components:

v = [x1, x2, x3, ..., xn]

This is an n-dimensional vector.

Vector as a Point

A vector can represent a point in space.

For example:

v = [3, 2]

can represent the point:

(3, 2)

This means:

x = 3
y = 2
Vector as a Direction

A vector can also represent movement.

v = [3, 2]

means:

Move 3 units in the x-direction
Move 2 units in the y-direction

Geometrically, this can be represented by an arrow.

Initial Point and Terminal Point

A vector has:

Initial Point

and:

Terminal Point

Example:

A = (1, 2)
B = (4, 6)

The vector from A to B is:

AB = B - A
AB = (4 - 1, 6 - 2)
AB = (3, 4)
Zero Vector

A zero vector contains only zeros.

Example:

0 = [0, 0]

or:

0 = [0, 0, 0]

The zero vector has:

Magnitude = 0

It has no specific direction.

Equal Vectors

Two vectors are equal if:

They have the same magnitude.
They have the same direction.

Example:

u = [2, 3]
v = [2, 3]

Therefore:

u = v

The starting positions do not matter for free vectors.

Vector Addition

To add two vectors, add their corresponding components.

Suppose:

u = [2, 3]
v = [4, 5]

Then:

u + v = [2 + 4, 3 + 5]
u + v = [6, 8]
Vector Subtraction

To subtract vectors, subtract their corresponding components.

u = [5, 7]
v = [2, 3]
u - v = [5 - 2, 7 - 3]
u - v = [3, 4]
Scalar Multiplication

A vector can be multiplied by a scalar.

Suppose:

v = [2, 3]

Then:

3v = 3[2, 3]
3v = [6, 9]

The scalar multiplies every component of the vector.

Negative Scalar Multiplication

Suppose:

v = [2, 3]

Then:

-2v = -2[2, 3]
-2v = [-4, -6]

A negative scalar reverses the direction of the vector.

Fractional Scalar Multiplication

A vector can also be multiplied by a fraction.

v = [10, 15]
1/5 v = 1/5 [10, 15]
1/5 v = [2, 3]

A fraction smaller than 1 reduces the magnitude of the vector.

Vector Magnitude

The magnitude of a vector is its length.

For a two-dimensional vector:

v = [x, y]

the magnitude is:

||v|| = √(x² + y²)
Example of Magnitude

Suppose:

v = [3, 4]

Then:

||v|| = √(3² + 4²)
||v|| = √(9 + 16)
||v|| = √25
||v|| = 5

Therefore:

Magnitude = 5
Magnitude of a 3D Vector

For:

v = [x, y, z]

the magnitude is:

||v|| = √(x² + y² + z²)

Example:

v = [2, 3, 6]
||v|| = √(2² + 3² + 6²)
||v|| = √(4 + 9 + 36)
||v|| = √49
||v|| = 7
Unit Vector

A unit vector is a vector with a magnitude of:

1

A unit vector represents direction without changing the length.

Finding a Unit Vector

To convert a vector into a unit vector:

Unit Vector = Vector / Magnitude of Vector

Suppose:

v = [3, 4]

Its magnitude is:

||v|| = 5

Therefore:

v̂ = v / ||v||
v̂ = [3, 4] / 5
v̂ = [3/5, 4/5]

or:

v̂ = [0.6, 0.8]

Its magnitude is:

1
Standard Unit Vectors

In 2D, the standard unit vectors are:

i = [1, 0]

and:

j = [0, 1]

Any two-dimensional vector can be written using these vectors.

Example:

v = [3, 2]

can be written as:

v = 3i + 2j
Standard Basis Vectors in 3D

In three dimensions, the standard basis vectors are:

i = [1, 0, 0]
j = [0, 1, 0]
k = [0, 0, 1]

A vector:

v = [2, 3, 4]

can be written as:

v = 2i + 3j + 4k
Linear Combination of Vectors

A linear combination is created by:

Multiplying vectors by scalars.
Adding the results.

Example:

u = [1, 0]
v = [0, 1]

Then:

3u + 2v

becomes:

3[1, 0] + 2[0, 1]
[3, 0] + [0, 2]
[3, 2]
Dot Product

The dot product is an operation between two vectors.

For:

u = [u1, u2]
v = [v1, v2]

the dot product is:

u · v = u1v1 + u2v2
Dot Product Example

Suppose:

u = [2, 3]
v = [4, 5]

Then:

u · v = (2 × 4) + (3 × 5)
u · v = 8 + 15
u · v = 23

The result of a dot product is a scalar.

Dot Product in 3D

Suppose:

u = [u1, u2, u3]
v = [v1, v2, v3]

Then:

u · v = u1v1 + u2v2 + u3v3

Example:

u = [1, 2, 3]
v = [4, 5, 6]
u · v = (1 × 4) + (2 × 5) + (3 × 6)
u · v = 4 + 10 + 18
u · v = 32
Geometric Dot Product

The dot product can also be calculated using:

u · v = ||u|| ||v|| cos(θ)

Where:

||u|| = Magnitude of u
||v|| = Magnitude of v
θ = Angle between the vectors

This formula connects vectors with geometry.

Orthogonal Vectors

Two vectors are orthogonal if they are perpendicular.

The angle between them is:

90 degrees

For orthogonal vectors:

u · v = 0

Example:

u = [1, 0]
v = [0, 1]
u · v = (1 × 0) + (0 × 1)
u · v = 0

Therefore, the vectors are orthogonal.

Angle Between Two Vectors

The dot product formula can be rearranged to calculate the angle:

cos(θ) = (u · v) / (||u|| ||v||)

Therefore:

θ = cos⁻¹((u · v) / (||u|| ||v||))

This formula calculates the angle between two vectors.

Vector Projection

The projection of one vector onto another shows how much of one vector points in the direction of another.

The scalar projection of u onto v is:

proj_length = (u · v) / ||v||

The vector projection is:

proj_v(u) = ((u · v) / (v · v))v

Vector projection is used in:

Physics
Computer Graphics
Geometry
Machine Learning
Vectors in Data Science

A data point can be represented as a vector.

Suppose a house has:

Size = 2000 square feet
Bedrooms = 3
Age = 10 years

We can represent it as:

x = [2000, 3, 10]

This is called a feature vector.

Feature Vectors in Machine Learning

Suppose we want to predict a student's marks.

The features could be:

Study Hours
Attendance
Previous Marks

A student can be represented as:

x = [5, 90, 75]

Each value is a feature.

Machine Learning algorithms use these feature vectors as input.

Vectors and Linear Regression

A linear regression model can be written as:

y = w1x1 + w2x2 + ... + wnxn + b

Using vectors, this becomes:

y = wᵀx + b

Where:

x = Feature Vector
w = Weight Vector
b = Bias
y = Prediction

This is an important application of vectors in Machine Learning.

Vectors in Neural Networks

Neural networks use vectors to represent:

Input data
Weights
Biases
Activations

A neuron performs an operation such as:

z = wᵀx + b

This is a dot product between:

Weight Vector

and:

Input Vector

Therefore, vectors are fundamental to neural networks.

Vectors in Natural Language Processing

In NLP, words can be represented as vectors.

For example:

"King" → [0.25, 0.71, -0.32, ...]

These vectors are called:

Word Embeddings

Words with similar meanings often have similar vector representations.

Examples:

King
Queen
Man
Woman

can be represented as vectors in a high-dimensional space.

Vectors in Computer Vision

Images can also be represented using vectors.

A grayscale image can be converted into pixel values:

[0, 255, 128, 64, ...]

These values can be represented as a vector.

A color image can contain even more values because each pixel has:

Red
Green
Blue

Machine Learning models process these numerical representations.

Vector Operations in Python

Python lists can represent vectors:

v = [2, 3, 4]

However, NumPy is commonly used for mathematical vector operations.

import numpy as np

v = np.array([2, 3, 4])
Vector Addition in NumPy
import numpy as np

u = np.array([2, 3])
v = np.array([4, 5])

result = u + v

print(result)

Output:

[6 8]
Scalar Multiplication in NumPy
v = np.array([2, 3])

result = 3 * v

print(result)

Output:

[6 9]
Vector Magnitude in NumPy
import numpy as np

v = np.array([3, 4])

magnitude = np.linalg.norm(v)

print(magnitude)

Output:

5.0
Dot Product in NumPy
u = np.array([2, 3])
v = np.array([4, 5])

result = np.dot(u, v)

print(result)

Output:

23

You can also use:

result = u @ v
Important Vector Formulas
Vector Addition
u + v = [u1 + v1, u2 + v2]
Scalar Multiplication
cv = [cv1, cv2, ..., cvn]
Magnitude
||v|| = √(v1² + v2² + ... + vn²)
Dot Product
u · v = u1v1 + u2v2 + ... + unvn
Unit Vector
v̂ = v / ||v||
Angle Between Vectors
θ = cos⁻¹((u · v) / (||u|| ||v||))
Final Summary

A vector is an ordered collection of numbers.

Vectors can represent:

Points
Directions
Magnitudes
Data features

The most important vector operations are:

Vector Addition
Vector Subtraction
Scalar Multiplication
Magnitude
Dot Product
Vector Projection

The most important concepts are:

Scalar
Vector
Components
Dimension
Magnitude
Unit Vector
Dot Product
Orthogonal Vectors
Linear Combination

Vectors are fundamental to:

Data Science
Machine Learning
Deep Learning
Natural Language Processing
Computer Vision
Robotics
Physics

The most important idea to remember is:

A vector is not just a list of numbers.

It can represent direction, magnitude, position,
or a collection of features in a dataset.

In Machine Learning:

Data → Vectors → Mathematical Operations → Predictions

And in Deep Learning:

Input Vectors
      ↓
Weight Vectors
      ↓
Dot Products
      ↓
Matrix Operations
      ↓
Predictions