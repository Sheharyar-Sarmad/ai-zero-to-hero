# Linear Combinations, Span, and Basis Vectors

## Linear Combination

A linear combination is created by multiplying vectors by scalars and then adding them together.

Suppose we have two vectors:

```text
u = [1, 0]
v = [0, 1]

We can create a new vector:

3u + 2v

Now substitute the vectors:

3[1, 0] + 2[0, 1]

Multiply the scalars:

[3, 0] + [0, 2]

Add the vectors:

[3, 2]

Therefore:

3u + 2v = [3, 2]

This is called a linear combination of u and v.

General Form of a Linear Combination

Suppose we have vectors:

v1, v2, v3, ..., vn

A linear combination is:

c1v1 + c2v2 + c3v3 + ... + cnvn

Where:

c1, c2, c3, ..., cn

are scalars.

Example:

2v1 + 5v2 - 3v3

is a linear combination of:

v1, v2, v3
Example of Linear Combination

Suppose:

v1 = [1, 2]
v2 = [3, 4]

Find:

2v1 + 3v2

First multiply:

2v1 = 2[1, 2]
2v1 = [2, 4]

Now:

3v2 = 3[3, 4]
3v2 = [9, 12]

Add the results:

[2, 4] + [9, 12]

Final answer:

[11, 16]

Therefore:

2v1 + 3v2 = [11, 16]
Span

The span of a set of vectors is the collection of all possible linear combinations of those vectors.

Suppose:

v1 = [1, 0]
v2 = [0, 1]

Their span is:

Span(v1, v2)

Every vector created using:

av1 + bv2

belongs to their span.

For example:

3v1 + 2v2 = [3, 2]

and:

10v1 - 5v2 = [10, -5]

Both vectors are inside the span of:

[1, 0]
[0, 1]
Span of Standard Basis Vectors

Consider:

e1 = [1, 0]
e2 = [0, 1]

Any 2D vector:

[x, y]

can be written as:

x[1, 0] + y[0, 1]

Therefore:

Span(e1, e2) = R²

This means these two vectors can create every vector in two-dimensional space.

Span in Two Dimensions

Suppose:

v1 = [1, 0]
v2 = [0, 1]

Their span covers the entire 2D plane.

We can create:

[3, 5]

using:

3v1 + 5v2

We can create:

[-2, 7]

using:

-2v1 + 7v2

Therefore, every point in the 2D plane can be reached.

Span of a Single Vector

Suppose:

v = [2, 3]

The span of v is:

Span(v) = {cv | c is a scalar}

Examples:

1v = [2, 3]
2v = [4, 6]
-1v = [-2, -3]

All these vectors lie on the same line.

Therefore:

Span([2, 3])

is a line through the origin.

Span and Geometry

The number of vectors and their directions determine the shape of their span.

One Non-Zero Vector

The span is:

A line
Two Independent Vectors in 2D

The span is:

The entire 2D plane
Three Independent Vectors in 3D

The span is:

The entire 3D space
Dependent Vectors and Span

Consider:

v1 = [1, 2]
v2 = [2, 4]

Notice:

v2 = 2v1

Therefore, both vectors point in the same direction.

Their span is only:

A line

They cannot create every vector in 2D space.

Independent Vectors

Vectors are linearly independent if no vector can be created as a linear combination of the other vectors.

Example:

v1 = [1, 0]
v2 = [0, 1]

Neither vector can be created using the other.

Therefore, they are linearly independent.

Dependent Vectors

Vectors are linearly dependent if at least one vector can be created using the other vectors.

Example:

v1 = [1, 2]
v2 = [2, 4]

Since:

v2 = 2v1

the vectors are linearly dependent.

Linear Independence Equation

A set of vectors is linearly independent if:

c1v1 + c2v2 + ... + cnvn = 0

has only the trivial solution:

c1 = c2 = ... = cn = 0

If there is a non-zero solution, the vectors are linearly dependent.

Basis Vectors

A basis is a set of vectors that:

Spans a vector space.
Is linearly independent.

Therefore:

Basis = Spanning + Linear Independence

A basis provides a set of fundamental directions from which all vectors in a space can be created.

Standard Basis of R²

The standard basis vectors of 2D space are:

e1 = [1, 0]
e2 = [0, 1]

These vectors are:

Linearly independent

and:

Span the entire R² space

Therefore:

{[1, 0], [0, 1]}

is a basis for:

R²
Standard Basis of R³

The standard basis vectors of 3D space are:

e1 = [1, 0, 0]
e2 = [0, 1, 0]
e3 = [0, 0, 1]

They can create any vector:

[x, y, z]

using:

xe1 + ye2 + ze3

Therefore:

{e1, e2, e3}

is the standard basis of:

R³
Example of a Different Basis

The standard basis is not the only possible basis.

Consider:

v1 = [1, 1]
v2 = [1, -1]

These vectors are linearly independent.

They can also span the entire 2D plane.

Therefore:

{[1, 1], [1, -1]}

is also a basis for:

R²
Coordinates Relative to a Basis

A vector can be represented using different bases.

Suppose:

v1 = [1, 1]
v2 = [1, -1]

We want to represent:

x = [4, 2]

as:

x = av1 + bv2

Substitute:

[4, 2] = a[1, 1] + b[1, -1]

This becomes:

[4, 2] = [a + b, a - b]

Therefore:

a + b = 4
a - b = 2

Solving:

a = 3
b = 1

Therefore:

[4, 2] = 3[1, 1] + 1[1, -1]
Basis and Dimension

The number of vectors in a basis is called the dimension of the vector space.

For example:

R²

has dimension:

2

because its basis contains two vectors.

The standard basis is:

[1, 0]
[0, 1]
Dimension of R³

The space:

R³

has dimension:

3

because its basis contains three vectors:

[1, 0, 0]
[0, 1, 0]
[0, 0, 1]
Linear Combination vs Span
Linear Combination

A linear combination creates one particular vector.

Example:

2v1 + 3v2 = [5, 7]
Span

The span represents all possible vectors that can be created.

Example:

Span(v1, v2)

means:

All possible combinations of v1 and v2
Basis vs Span
Span

The span is the complete set of vectors that can be created.

Span(v1, v2)
Basis

A basis is a minimal set of vectors that:

Spans the space

and:

Contains no redundant vectors
Important Relationship

The relationship can be summarized as:

Vectors
    ↓
Linear Combinations
    ↓
All Possible Combinations
    ↓
Span
    ↓
Independent Spanning Set
    ↓
Basis
Linear Combinations in Machine Learning

Machine Learning data is represented using vectors.

Suppose:

x = [Age, Salary, Experience]

A model can calculate:

w1x1 + w2x2 + w3x3

This is a linear combination of features.

For example:

y = 2x1 + 5x2 + 3x3

The model combines different features using weights.

This is one of the basic ideas behind:

Linear Regression
Neural Networks
Machine Learning Models
Feature Vectors and Basis

Suppose a dataset has three features:

Age
Salary
Experience

A data point can be represented as:

x = [25, 50000, 3]

These features create a point in a three-dimensional feature space.

The feature vectors can be treated as coordinates in a vector space.

Linear Combination in Neural Networks

A neuron calculates a weighted combination of inputs.

Suppose:

x = [x1, x2, x3]

and:

w = [w1, w2, w3]

The neuron calculates:

z = w1x1 + w2x2 + w3x3 + b

The expression:

w1x1 + w2x2 + w3x3

is a linear combination.

Python Example

Using NumPy:

import numpy as np

v1 = np.array([1, 0])
v2 = np.array([0, 1])

result = 3 * v1 + 2 * v2

print(result)

Output:

[3 2]

This demonstrates a linear combination.

Checking Linear Dependence

Consider:

import numpy as np

v1 = np.array([1, 2])
v2 = np.array([2, 4])

We can see:

v2 = 2 * v1

Therefore:

v1 and v2 are linearly dependent
Important Definitions
Linear Combination

A combination of vectors multiplied by scalars and added together.

c1v1 + c2v2 + ... + cnvn
Span

The set of all possible linear combinations of a set of vectors.

Linearly Independent

No vector can be created using the other vectors.

Linearly Dependent

At least one vector can be created using the other vectors.

Basis

A linearly independent set of vectors that spans a vector space.

Dimension

The number of vectors in a basis.

Final Summary

A linear combination is:

Scalar × Vector + Scalar × Vector

The span is:

All possible linear combinations

A basis is:

A linearly independent spanning set

The key relationship is:

Linear Combination
        ↓
       Span
        ↓
Independent Span
        ↓
      Basis

The most important concepts to remember are:

Linear Combination
Span
Linear Independence
Linear Dependence
Basis
Dimension

These concepts are fundamental to:

Linear Algebra
Data Science
Machine Learning
Deep Learning
Computer Graphics
Physics