# Linear Transformations and Matrices

## What is a Linear Transformation?

A linear transformation is a function that maps vectors from one vector space to another while preserving linear relationships.

A transformation is usually written as:

T(v)

For a vector:

v = [x, y]

a transformation changes the vector into another vector.

Example:

T([x, y]) = [2x, 2y]

This transformation doubles the vector.

---

# Conditions of a Linear Transformation

A transformation is linear if it satisfies two important properties:

1. Additivity
2. Scalar Multiplication

---

## 1. Additivity

A linear transformation must satisfy:

T(u + v) = T(u) + T(v)

This means transforming the sum of two vectors gives the same result as transforming both vectors separately and then adding the results.

---

## Example

Suppose:

T(x, y) = (2x, 2y)

Let:

u = [1, 2]

v = [3, 4]

First:

u + v = [4, 6]

Apply the transformation:

T(u + v) = [8, 12]

Now transform separately:

T(u) = [2, 4]

T(v) = [6, 8]

Add:

T(u) + T(v) = [8, 12]

Therefore:

T(u + v) = T(u) + T(v)

---

# 2. Scalar Multiplication

A linear transformation must satisfy:

T(cv) = cT(v)

Where:

c = Scalar

v = Vector

---

## Example

Suppose:

T(x, y) = (2x, 2y)

Let:

v = [2, 3]

and:

c = 4

First:

cv = 4[2, 3]

cv = [8, 12]

Apply the transformation:

T(cv) = [16, 24]

Now:

T(v) = [4, 6]

cT(v) = 4[4, 6]

cT(v) = [16, 24]

Therefore:

T(cv) = cT(v)

---

# Important Condition

A transformation is linear if:

T(u + v) = T(u) + T(v)

and:

T(cv) = cT(v)

Together:

T(au + bv) = aT(u) + bT(v)

This means linear transformations preserve linear combinations.

---

# Examples of Linear Transformations

Common linear transformations include:

- Scaling
- Rotation
- Reflection
- Shearing
- Projection

These transformations can be represented using matrices.

---

# Transformation of a Vector

Suppose:

v = [x, y]

A transformation can change it to:

T(v) = [x', y']

For example:

T([x, y]) = [2x, 3y]

This transformation:

- Doubles the x-coordinate
- Triples the y-coordinate

---

# Matrices and Linear Transformations

Matrices are used to represent linear transformations.

Suppose:

A =

[2  0]
[0  3]

and:

v =

[x]
[y]

Then:

Av =

[2  0] [x]
[0  3] [y]

The result is:

[2x]
[3y]

Therefore:

T(v) = Av

This is the fundamental relationship:

Transformation = Matrix × Vector

---

# Matrix Transformation Example

Suppose:

A =

[2  0]
[0  3]

and:

v =

[1]
[2]

Then:

Av =

[2  0] [1]
[0  3] [2]

Calculate:

First component:

2(1) + 0(2) = 2

Second component:

0(1) + 3(2) = 6

Therefore:

Av =

[2]
[6]

The original vector:

[1, 2]

becomes:

[2, 6]

---

# Matrix as a Function

A matrix can be treated as a function.

For example:

A(v) = Av

This means the matrix takes a vector as input and produces another vector as output.

Input:

v

Transformation:

A

Output:

Av

Therefore:

Vector → Matrix Transformation → New Vector

---

# Standard Basis Vectors

In two dimensions, the standard basis vectors are:

e1 = [1, 0]

e2 = [0, 1]

Any vector:

v = [x, y]

can be written as:

v = xe1 + ye2

This is important because a matrix transformation can be completely understood by observing what it does to the basis vectors.

---

# Matrix Columns and Basis Vectors

Consider the matrix:

A =

[2  3]
[1  4]

Its columns are:

First column:

[2]
[1]

Second column:

[3]
[4]

These columns represent:

A(e1) = [2, 1]

A(e2) = [3, 4]

Therefore, the columns of a matrix are the transformed basis vectors.

---

# Important Matrix Concept

For a matrix:

A =

[a  b]
[c  d]

we have:

A(e1) =

[a]
[c]

and:

A(e2) =

[b]
[d]

Therefore:

Matrix columns = Images of the standard basis vectors

---

# Scaling Transformation

Scaling changes the size of a vector.

Example:

A =

[2  0]
[0  3]

This transformation:

- Multiplies the x-coordinate by 2
- Multiplies the y-coordinate by 3

For:

v = [1, 1]

the result is:

Av = [2, 3]

---

# Uniform Scaling

Uniform scaling changes all dimensions by the same amount.

Matrix:

A =

[2  0]
[0  2]

For:

v = [3, 4]

we get:

Av = [6, 8]

The direction remains the same.

The magnitude becomes twice as large.

---

# Non-Uniform Scaling

Non-uniform scaling uses different scaling factors.

Matrix:

A =

[2  0]
[0  3]

The x-direction is scaled by 2.

The y-direction is scaled by 3.

This can change the shape of objects.

---

# Rotation Transformation

A rotation changes the direction of a vector.

The 2D rotation matrix is:

R(θ) =

[cos(θ)  -sin(θ)]
[sin(θ)   cos(θ)]

Where:

θ = Angle of rotation

---

# Rotation by 90 Degrees

For a 90-degree counterclockwise rotation:

R =

[0  -1]
[1   0]

Suppose:

v =

[1]
[0]

Then:

Rv =

[0]
[1]

The vector:

[1, 0]

becomes:

[0, 1]

---

# Reflection Transformation

Reflection flips a vector or object across an axis.

Reflection across the x-axis:

A =

[1   0]
[0  -1]

For:

v = [x, y]

the result is:

[x, -y]

The x-coordinate remains the same.

The y-coordinate changes sign.

---

# Reflection Across the y-axis

The matrix is:

A =

[-1  0]
[0   1]

For:

v = [x, y]

the result is:

[-x, y]

---

# Shearing Transformation

Shearing changes the shape of an object by shifting one direction.

Horizontal shear:

A =

[1  k]
[0  1]

The transformation is:

x' = x + ky

y' = y

---

# Matrix Multiplication and Transformations

Multiple transformations can be combined using matrix multiplication.

Suppose:

A = First Transformation

B = Second Transformation

Applying A first and then B:

v' = BAv

The combined transformation is:

BA

Therefore:

Multiple Transformations = Matrix Multiplication

---

# Example of Combined Transformations

Suppose:

A scales a vector.

B rotates a vector.

First:

v1 = Av

Then:

v2 = Bv1

Substitute:

v2 = B(Av)

Therefore:

v2 = BAv

The combined transformation is:

BA.

---

# Order Matters

Matrix multiplication is generally not commutative.

This means:

AB ≠ BA

Applying transformation A followed by B can produce a different result than applying B followed by A.

Therefore:

Order of Transformations Matters.

---

# Identity Transformation

The identity matrix does not change a vector.

In 2D:

I =

[1  0]
[0  1]

For any vector:

Iv = v

Example:

I[3, 5] = [3, 5]

The identity matrix is the equivalent of the number 1 in normal multiplication.

---

# Zero Transformation

The zero matrix transforms every vector into the zero vector.

Example:

A =

[0  0]
[0  0]

Then:

Av = [0, 0]

for every vector v.

---

# Inverse Transformation

An inverse transformation reverses the effect of a transformation.

If:

Av = w

then:

A⁻¹w = v

Therefore:

A⁻¹A = I

The inverse matrix returns the vector to its original state.

---

# Example of an Inverse

Suppose:

A =

[2  0]
[0  2]

This doubles a vector.

Its inverse is:

A⁻¹ =

[1/2  0]
[0   1/2]

If:

v = [3, 4]

then:

Av = [6, 8]

Applying the inverse:

A⁻¹[6, 8] = [3, 4]

The original vector is restored.

---

# Determinant and Transformations

The determinant tells us important information about a matrix transformation.

For:

A =

[a  b]
[c  d]

the determinant is:

det(A) = ad - bc

---

# Geometric Meaning of the Determinant

The absolute value of the determinant represents the area scaling factor.

If:

det(A) = 2

the area is multiplied by 2.

If:

det(A) = 0.5

the area is reduced to half.

If:

det(A) = 0

the transformation collapses space into a lower dimension.

---

# Determinant and Inverse

A matrix has an inverse if:

det(A) ≠ 0

A matrix does not have an inverse if:

det(A) = 0

When the determinant is zero, the transformation loses information.

---

# Rank of a Transformation

The rank of a matrix tells us the dimension of the space produced by the transformation.

For example:

A full-rank 2D transformation can map the plane to the plane.

A rank-1 transformation may collapse the plane into a line.

A rank-0 transformation maps everything to the zero vector.

---

# Linear Transformation and Span

A linear transformation preserves linear combinations.

If:

v = av1 + bv2

then:

T(v) = aT(v1) + bT(v2)

This means:

T(av1 + bv2) = aT(v1) + bT(v2)

This is one of the most important properties of linear transformations.

---

# Matrix Representation

Every linear transformation between finite-dimensional vector spaces can be represented using a matrix.

For example:

T(v) = Av

where:

A = Transformation Matrix

v = Input Vector

Av = Output Vector

---

# Linear Transformations in Machine Learning

Linear transformations are fundamental to Machine Learning.

A linear model can be written as:

y = wx + b

For multiple features:

y = w1x1 + w2x2 + ... + wnxn + b

Using vectors:

y = wᵀx + b

This involves:

- Vectors
- Dot Products
- Matrix Operations

---

# Linear Transformations in Neural Networks

A neural network layer commonly performs:

z = Wx + b

Where:

W = Weight Matrix

x = Input Vector

b = Bias Vector

z = Output Vector

The matrix W performs a linear transformation.

The bias b shifts the result.

---

# Important Note About Neural Networks

Strictly speaking:

Wx + b

is an affine transformation rather than a pure linear transformation because of the bias term.

A pure linear transformation is:

Wx

An affine transformation is:

Wx + b

---

# Matrix Transformation Using NumPy

```python
import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

v = np.array([1, 2])

result = A @ v

print(result)

The vector is rotated by 90 degrees.

Summary

A linear transformation changes vectors while preserving:

Vector addition
Scalar multiplication
Linear combinations

The main equation is:

T(v) = Av

Where:

A = Transformation Matrix

v = Input Vector

Av = Transformed Vector

Important transformations include:

Scaling
Rotation
Reflection
Shearing
Projection

Important matrix concepts include:

Matrix multiplication
Identity matrix
Inverse matrix
Determinant
Rank

The key idea is:

Vector → Matrix → Transformed Vector

In Machine Learning:

Input Vector → Weight Matrix → Output Vector

And in Neural Networks:

z = Wx + b

Understanding linear transformations and matrices is essential for:

Machine Learning
Deep Learning
Computer Vision
Computer Graphics
Robotics
Physics