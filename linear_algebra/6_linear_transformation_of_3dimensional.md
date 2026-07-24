Three-Dimensional Linear Transformations
1. What is a Linear Transformation?

A linear transformation is a function that maps vectors from one vector space to another while preserving:

Vector addition
Scalar multiplication

For a transformation T:

T(u + v) = T(u) + T(v)

T(cu) = cT(u)

In machine learning, linear transformations are mainly represented using matrices.

2. Vectors in Three Dimensions

A vector in 3D space has three components:

v = [x, y, z]

Example:

v = [2, 3, 1]

Geometrically, this vector can be represented as an arrow from the origin:

(0, 0, 0) → (2, 3, 1)

The three axes are:

x-axis: left/right
y-axis: up/down
z-axis: depth
3. Matrix Representation

A 3D linear transformation is commonly represented by a 3 × 3 matrix:

A =

[a b c]
[d e f]
[g h i]

When this matrix multiplies a 3D vector:

Av =

[a b c] [x]
[d e f] [y]
[g h i] [z]

The result is another 3D vector:

Av =

[ax + by + cz]
[dx + ey + fz]
[gx + hy + iz]

So, a matrix transforms one vector into another.

4. The Standard Basis Vectors

Every 3D vector can be represented using the standard basis vectors:

e₁ = [1, 0, 0]

e₂ = [0, 1, 0]

e₃ = [0, 0, 1]

For a vector:

v = [x, y, z]

we can write:

v = xe₁ + ye₂ + ze₃

This means every 3D vector is a linear combination of the basis vectors.

5. The Matrix Columns Represent Transformed Basis Vectors

One of the most important ideas:

The columns of a transformation matrix tell us where the basis vectors go.

For:

A =

[a b c]
[d e f]
[g h i]

The columns are:

Ae₁ = [a, d, g]

Ae₂ = [b, e, h]

Ae₃ = [c, f, i]

Therefore:

A = [Ae₁ Ae₂ Ae₃]

This gives a powerful geometric interpretation of a matrix.

A 3D transformation is completely determined by what it does to the three basis vectors.

6. Example of a 3D Transformation

Suppose:

A =

[2 0 0]
[0 3 0]
[0 0 1]

and:

v =

[1]
[2]
[3]

Then:

Av =

[2 × 1 + 0 × 2 + 0 × 3]
[0 × 1 + 3 × 2 + 0 × 3]
[0 × 1 + 0 × 2 + 1 × 3]

Therefore:

Av =

[2]
[6]
[3]

The transformation:

Doubles the x-coordinate
Triples the y-coordinate
Leaves the z-coordinate unchanged

This is called scaling.

7. Important Types of 3D Linear Transformations
Scaling

Scaling changes the size of an object or vector.

A general scaling matrix is:

S =

[sₓ 0 0]
[0 sᵧ 0]
[0 0 s𝓏]

The transformation is:

[x]
[y]
[z]

→

[sₓx]
[sᵧy]
[s𝓏z]

Example:

S =

[2 0 0]
[0 3 0]
[0 0 4]

This means:

x is scaled by 2
y is scaled by 3
z is scaled by 4
Rotation

Rotation changes the direction of a vector while usually preserving its length.

Rotation around the x-axis:

Rₓ(θ) =

[1 0 0]
[0 cosθ -sinθ]
[0 sinθ cosθ]

Rotation around the y-axis:

Rᵧ(θ) =

[ cosθ 0 sinθ]
[ 0 1 0 ]
[-sinθ 0 cosθ]

Rotation around the z-axis:

R𝓏(θ) =

[cosθ -sinθ 0]
[sinθ cosθ 0]
[ 0 0 1]

Rotations are extremely important in:

Computer graphics
Computer vision
Robotics
3D object recognition
Spatial data
Reflection

Reflection flips a vector across a plane.

Reflection across the yz-plane:

R =

[-1 0 0]
[ 0 1 0]
[ 0 0 1]

This changes:

(x, y, z)

to:

(-x, y, z)

Reflection across the xz-plane:

(x, y, z)

→

(x, -y, z)

Reflection across the xy-plane:

(x, y, z)

→

(x, y, -z)

Shearing

Shearing slants the shape while preserving some dimensions.

Example:

A =

[1 k 0]
[0 1 0]
[0 0 1]

Then:

x' = x + ky

y' = y

z' = z

The amount of shearing is controlled by k.

8. Linear Transformation of a 3D Vector

Suppose:

A =

[2 1 0]
[0 1 1]
[1 0 1]

and:

v =

[1]
[2]
[3]

Then:

Av =

[2(1) + 1(2) + 0(3)]
[0(1) + 1(2) + 1(3)]
[1(1) + 0(2) + 1(3)]

Av =

[4]
[5]
[4]

So:

[1, 2, 3] → [4, 5, 4]

The matrix transforms the original vector into a new vector.

9. Linear Transformation of the Entire 3D Space

A matrix does not only transform one vector.

It transforms every vector in the entire space.

For example:

T(v) = Av

For every possible:

v ∈ R³

the matrix A determines a corresponding output vector.

Therefore:

T: R³ → R³

A transformation can:

Stretch space
Compress space
Rotate space
Reflect space
Shear space
Collapse dimensions
10. The Determinant and Volume

The determinant tells us how a transformation changes volume.

For a 3 × 3 matrix:

det(A)

represents the volume scaling factor.

If:

|det(A)| > 1

Volume increases.

If:

0 < |det(A)| < 1

Volume decreases.

If:

|det(A)| = 1

Volume remains the same.

If:

det(A) = 0

The 3D space collapses into a lower-dimensional space.

For example:

3D → 2D

or:

3D → 1D

This means the transformation is not invertible.

11. Determinant and Orientation

The sign of the determinant also matters.

If:

det(A) > 0

The orientation is preserved.

If:

det(A) < 0

The orientation is reversed.

A reflection usually changes the sign of the determinant.

12. Invertible Transformations

A transformation is invertible if we can reverse it.

If:

y = Ax

then:

x = A⁻¹y

Therefore:

A⁻¹A = I

where I is the identity matrix:

I =

[1 0 0]
[0 1 0]
[0 0 1]

A matrix is invertible when:

det(A) ≠ 0

13. Composition of 3D Transformations

Multiple transformations can be combined using matrix multiplication.

Suppose:

First apply B:

v → Bv

Then apply A:

Bv → A(Bv)

The complete transformation is:

ABv

Therefore:

AB = A ∘ B

Important:

The rightmost matrix is applied first.

For:

ABv

the order is:

Apply B
Apply A

Matrix multiplication is generally not commutative:

AB ≠ BA

This is very important in 3D transformations.

For example:

Rotate then scale
Scale then rotate

can produce different results.

14. 3D Linear Transformations in Machine Learning

In machine learning, data is often represented as vectors.

For example, a data point may be:

x =

[age]
[income]
[experience]

A matrix transformation can transform the feature vector:

x' = Wx

where:

x = input vector
W = weight matrix
x' = transformed vector

This is exactly the mathematical foundation of a neural network layer.

A neural network layer often performs:

z = Wx + b

The part:

Wx

is a linear transformation.

The bias:

b

then shifts the result.

15. Neural Networks and Linear Transformations

Suppose:

x =

[x₁]
[x₂]
[x₃]

and:

W =

[w₁₁ w₁₂ w₁₃]
[w₂₁ w₂₂ w₂₃]
[w₃₁ w₃₂ w₃₃]

Then:

Wx =

[w₁₁x₁ + w₁₂x₂ + w₁₃x₃]
[w₂₁x₁ + w₂₂x₂ + w₂₃x₃]
[w₃₁x₁ + w₃₂x₂ + w₃₃x₃]

This creates a new representation of the input data.

Then a neural network usually applies an activation function:

a = σ(Wx + b)

For example:

ReLU:

ReLU(x) = max(0, x)

The matrix performs the linear transformation.

The activation function introduces non-linearity.

16. Why Neural Networks Need Non-Linearity

A composition of only linear transformations is still a linear transformation.

For example:

T₁(x) = A₁x

T₂(x) = A₂x

Then:

T₂(T₁(x)) = A₂A₁x

This is still linear.

Therefore, stacking only matrix multiplications does not create a truly powerful deep network.

Activation functions such as:

ReLU
Sigmoid
Tanh

introduce non-linearity.

A typical neural network layer is:

Output = Activation(Wx + b)

17. Linear Transformation of a Dataset

Suppose we have a dataset:

X ∈ Rⁿˣᵈ

where:

n = number of samples
d = number of features

A transformation matrix:

W ∈ Rᵐˣᵈ

can transform the data:

Z = XWᵀ

Then:

Z ∈ Rⁿˣᵐ

This changes the feature representation.

For example:

Original data:

10 features

After transformation:

3 features

This is closely related to:

Feature transformation
Dimensionality reduction
PCA
Neural network embeddings
Representation learning
18. Connection to PCA

Principal Component Analysis (PCA) finds new directions in the data.

The data is transformed using a matrix:

Z = XW

The columns of W represent new directions, called principal components.

PCA attempts to find directions that capture maximum variance.

So, PCA can be understood as a linear transformation that changes the coordinate system of the data.

19. Important Intuition

A matrix is not just a table of numbers.

A matrix represents a transformation.

In 3D:

A matrix can transform:

Vectors
Points
Directions
Shapes
Coordinate systems
Feature representations

The most important mental model is:

Input vector
     ↓
   Matrix
     ↓
Transformed vector

In machine learning:

Input features
      ↓
Weight matrix W
      ↓
New feature representation
      ↓
Activation function
      ↓
Next layer
20. Summary
A 3D vector has three components: x, y, and z.
A 3D linear transformation is usually represented by a 3 × 3 matrix.
Matrix multiplication transforms vectors.
The columns of a matrix represent where the standard basis vectors go.
Scaling changes size.
Rotation changes direction.
Reflection flips space.
Shearing slants space.
The determinant describes volume scaling and orientation.
det(A) = 0 means the transformation collapses dimensions.
Matrix multiplication represents composition of transformations.
The rightmost matrix is applied first.
Neural network layers use linear transformations in the form Wx + b.
Activation functions add non-linearity.
PCA and many machine learning techniques use linear transformations to create new feature representations.

Core idea to remember:

A matrix is a function that transforms vectors.

And in AI/ML:

A neural network learns the best transformation matrix to convert input data into useful representations.