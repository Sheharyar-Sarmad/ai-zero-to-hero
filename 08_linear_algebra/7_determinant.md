Determinant
1. What is a Determinant?

A determinant is a single number calculated from a square matrix.

It provides important information about the matrix and the linear transformation represented by that matrix.

For a matrix A, the determinant is written as:

det(A)

or:

|A|

The determinant is only defined for square matrices.

Examples:

2 × 2 matrix
3 × 3 matrix
4 × 4 matrix

A 2 × 3 matrix does not have a determinant.

2. Determinant of a 2 × 2 Matrix

For:

A =

[a b]
[c d]

The determinant is:

det(A) = ad - bc

Example:

A =

[3 2]
[1 4]

det(A) = (3 × 4) - (2 × 1)

det(A) = 12 - 2

det(A) = 10

Therefore:

det(A) = 10

3. Geometric Meaning of the Determinant

The determinant tells us how a linear transformation changes area or volume.

For a 2D transformation:

det(A) = Area scaling factor

For a 3D transformation:

det(A) = Volume scaling factor

Example:

If:

det(A) = 3

Then the transformation makes the area or volume 3 times larger.

If:

det(A) = 0.5

Then the area or volume becomes half as large.

4. Determinant and Area

Consider two vectors:

u = [a, c]

v = [b, d]

The parallelogram formed by these vectors has area:

Area = |ad - bc|

Therefore:

Area = |det(A)|

where:

A =

[a b]
[c d]

The absolute value is used because area cannot be negative.

5. Determinant of a 3 × 3 Matrix

For:

A =

[a b c]
[d e f]
[g h i]

The determinant is:

det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)

This is called expansion by the first row.

Example:

A =

[1 2 3]
[0 4 5]
[1 0 6]

det(A) =

1(4 × 6 - 5 × 0)

2(0 × 6 - 5 × 1)
+ 3(0 × 0 - 4 × 1)

det(A) =

1(24)

2(-5)
+ 3(-4)

det(A) = 24 + 10 - 12

det(A) = 22

6. The Most Important Case: det(A) = 0

If:

det(A) = 0

then the matrix is singular.

A singular matrix:

Is not invertible
Loses information
Collapses dimensions
Maps space into a lower-dimensional space

For example:

3D space may collapse into a plane.

Or:

2D space may collapse into a line.

This is extremely important in machine learning.

7. Invertibility

A square matrix A is invertible if:

det(A) ≠ 0

A is not invertible if:

det(A) = 0

Therefore:

det(A) ≠ 0

means:

A⁻¹ exists

And:

det(A) = 0

means:

A⁻¹ does not exist

8. Determinant and Linear Independence

The determinant can tell us whether vectors are linearly independent.

For a matrix whose columns are vectors:

A = [v₁ v₂ ... vₙ]

If:

det(A) ≠ 0

then the vectors are linearly independent.

If:

det(A) = 0

then the vectors are linearly dependent.

For example, in 2D:

u = [1, 2]

v = [2, 4]

The second vector is:

v = 2u

Therefore, the vectors lie on the same line.

They are linearly dependent.

The determinant is:

det([1 2; 2 4])

= 1(4) - 2(2)

= 4 - 4

= 0

9. Determinant and Transformation

Suppose:

y = Ax

The determinant tells us how the transformation changes space.

det(A) > 1

Space expands.

0 < det(A) < 1

Space contracts.

det(A) = 1

Area or volume is preserved.

det(A) = -1

Area or volume is preserved, but orientation is reversed.

det(A) = 0

Space collapses into a lower dimension.

10. Negative Determinants

A determinant can be negative.

The absolute value represents the area or volume scaling factor.

The negative sign represents a change in orientation.

For example:

det(A) = -2

means:

Area or volume is scaled by 2
Orientation is reversed

Reflections often have negative determinants.

11. Determinant of the Identity Matrix

The identity matrix is:

I =

[1 0]
[0 1]

Its determinant is:

det(I) = 1

For a 3 × 3 identity matrix:

I =

[1 0 0]
[0 1 0]
[0 0 1]

det(I) = 1

The identity transformation does not change area or volume.

12. Determinant of a Diagonal Matrix

For:

A =

[a 0 0]
[0 b 0]
[0 0 c]

The determinant is:

det(A) = abc

Example:

A =

[2 0 0]
[0 3 0]
[0 0 4]

det(A) = 2 × 3 × 4

det(A) = 24

The transformation scales the volume by 24.

13. Determinant of a Triangular Matrix

For an upper or lower triangular matrix:

A =

[a b c]
[0 d e]
[0 0 f]

The determinant is simply:

det(A) = adf

The determinant is the product of the diagonal elements.

This is very useful computationally.

14. Important Determinant Properties
Property 1: Identity Matrix

det(I) = 1

Property 2: Product of Matrices

det(AB) = det(A)det(B)

This is very important for compositions of transformations.

If:

v → Bv → A(Bv)

then:

det(AB) = det(A)det(B)

The total scaling factor is the product of the individual scaling factors.

Property 3: Transpose

det(Aᵀ) = det(A)

Transposing a matrix does not change its determinant.

Property 4: Inverse

If A is invertible:

det(A⁻¹) = 1 / det(A)

Property 5: Scalar Multiplication

For an n × n matrix:

det(cA) = cⁿ det(A)

For a 3 × 3 matrix:

det(cA) = c³det(A)

15. Determinant and Eigenvalues

The determinant is related to eigenvalues.

For an n × n matrix:

det(A) = λ₁λ₂...λₙ

The determinant equals the product of all eigenvalues.

Example:

If the eigenvalues are:

λ₁ = 2

λ₂ = 3

λ₃ = 4

Then:

det(A) = 2 × 3 × 4

det(A) = 24

This connects determinants to:

Eigenvalues
Eigenvectors
PCA
Stability analysis
Machine learning
16. Determinant and the Characteristic Equation

Eigenvalues are found using:

det(A - λI) = 0

This equation is called the characteristic equation.

The determinant helps us find values of λ for which:

A - λI

becomes singular.

These values are the eigenvalues.

17. Determinant in Systems of Equations

Consider:

Ax = b

If:

det(A) ≠ 0

then the system has a unique solution.

If:

det(A) = 0

then the system may have:

No solution
Infinitely many solutions

The determinant helps us understand the structure of the system.

18. Cramer's Rule

For a system of equations:

Ax = b

Cramer's Rule can be used when:

det(A) ≠ 0

For a 2 × 2 system:

a₁x + b₁y = c₁

a₂x + b₂y = c₂

The coefficient matrix is:

A =

[a₁ b₁]
[a₂ b₂]

If:

det(A) ≠ 0

then the system has a unique solution.

However, in practical machine learning, Cramer's Rule is usually not used for large systems because it is computationally inefficient.

19. Determinant and Machine Learning

Determinants are important in several areas of AI and machine learning.

1. Checking Matrix Invertibility

A model may need to determine whether a matrix can be inverted.

If:

det(A) = 0

then:

A⁻¹ does not exist.

2. Covariance Matrices

A covariance matrix describes relationships between features.

For example:

X =

[height]
[weight]
[income]

The covariance matrix may be:

Σ

The determinant:

det(Σ)

is related to the volume of the uncertainty region of the data.

A larger determinant generally represents greater spread across multiple dimensions.

3. Multivariate Gaussian Distribution

The multivariate Gaussian probability density function contains:

det(Σ)

The formula includes:

1 / √det(Σ)

The determinant of the covariance matrix affects the normalization of the probability distribution.

This is important in:

Gaussian Mixture Models
Bayesian Machine Learning
Probabilistic Models
Generative Models
20. Determinant in PCA

PCA uses covariance matrices.

The covariance matrix is:

Σ

Its eigenvalues represent variance along principal directions.

The determinant of the covariance matrix is related to the product of the eigenvalues:

det(Σ) = λ₁λ₂...λₙ

This represents the generalized variance of the data.

21. Determinant in Deep Learning

Determinants appear in certain deep learning models.

For example:

Normalizing Flows transform probability distributions.

Suppose:

z = f(x)

To calculate probability density after transformation, we need the Jacobian determinant:

det(J)

The change-of-variables formula includes:

pₓ(x) = p_z(f(x)) |det(J)|

This tells us how the transformation changes probability density.

22. Jacobian Determinant

For a function:

f: Rⁿ → Rⁿ

the Jacobian matrix contains partial derivatives.

For:

f(x, y) =

[f₁(x, y)]
[f₂(x, y)]

The Jacobian is:

J =

[∂f₁/∂x ∂f₁/∂y]
[∂f₂/∂x ∂f₂/∂y]

The determinant:

det(J)

describes the local area scaling caused by the function.

In 3D:

det(J)

describes local volume scaling.

This is very important in:

Physics-informed ML
Computer vision
Robotics
Normalizing flows
Differential geometry
23. Determinant and Numerical Stability

In machine learning, directly calculating determinants can sometimes be numerically unstable.

Instead of calculating:

det(A)

we often calculate:

log|det(A)|

This is called the log-determinant.

For large matrices, the log-determinant is more numerically stable.

For example:

log det(A)

is commonly used in:

Gaussian likelihoods
Covariance matrices
Probabilistic models
Normalizing flows
24. Determinant in NumPy

Using NumPy:

import numpy as np

A = np.array([
    [3, 2],
    [1, 4]
])

det_A = np.linalg.det(A)

print(det_A)

Output:

10.0

For a 3 × 3 matrix:

A = np.array([
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
])

det_A = np.linalg.det(A)

print(det_A)

Output:

22.0
25. Checking if a Matrix is Invertible
import numpy as np

A = np.array([
    [1, 2],
    [2, 4]
])

det_A = np.linalg.det(A)

if det_A == 0:
    print("Matrix is singular")
else:
    print("Matrix is invertible")

However, with floating-point numbers, it is safer to use:

if np.isclose(det_A, 0):
    print("Matrix is singular")
else:
    print("Matrix is invertible")

Because floating-point calculations may produce very small values such as:

0.00000000001

instead of exactly:

0
26. Determinant vs Matrix Inverse

These concepts are closely related:

det(A) ≠ 0
      ↓
A is invertible
      ↓
A⁻¹ exists

But:

det(A) = 0
      ↓
A is singular
      ↓
A⁻¹ does not exist
27. Simple Mental Model

Think of a matrix as transforming space.

Before transformation:

Square

After transformation:

Larger square

The determinant tells you how much the area changed.

In 3D:

Cube

After transformation:

Larger or smaller parallelepiped

The determinant tells you the volume scaling.

28. AI/ML Mental Model

For AI and ML, remember:

Matrix
   ↓
Linear transformation
   ↓
Space changes
   ↓
Determinant measures
area/volume scaling

And:

det(A) = 0
      ↓
Information is lost
      ↓
Matrix cannot be inverted
29. Key Takeaways
A determinant is a scalar value calculated from a square matrix.
It measures area scaling in 2D.
It measures volume scaling in 3D.
det(A) = 0 means the matrix is singular.
det(A) ≠ 0 means the matrix is invertible.
A nonzero determinant indicates linear independence of the matrix columns.
A negative determinant indicates reversed orientation.
det(AB) = det(A)det(B).
The determinant equals the product of eigenvalues.
Determinants are important in covariance matrices and PCA.
Jacobian determinants measure local area or volume changes.
Normalizing flows use Jacobian determinants to transform probability distributions.
In numerical machine learning, log-determinants are often preferred for stability.

The most important idea:

The determinant tells you how a matrix transformation changes space and whether information has been lost.