# Inverse Matrices, Column Space, and Null Space

These are important concepts in Linear Algebra and are widely used in AI and Machine Learning.

---

# 1. Inverse Matrix

The inverse of a matrix reverses the transformation performed by the original matrix.

For a matrix A, its inverse is written as:

A⁻¹

The main property is:

A⁻¹A = AA⁻¹ = I

where I is the identity matrix.

---

## Identity Matrix

For a 2 × 2 matrix:

I =

[1  0]
[0  1]

The identity matrix does not change a vector:

Iv = v

---

# 2. Inverse Matrix and Linear Systems

Consider:

Ax = b

If A is invertible, multiply both sides by A⁻¹:

A⁻¹Ax = A⁻¹b

Since:

A⁻¹A = I

we get:

x = A⁻¹b

Therefore, the inverse matrix can be used to solve systems of linear equations.

---

# 3. When Does an Inverse Exist?

A square matrix A is invertible if:

det(A) ≠ 0

If:

det(A) = 0

then A is singular and its inverse does not exist.

```text
det(A) ≠ 0 → Invertible → A⁻¹ exists
det(A) = 0 → Singular → A⁻¹ does not exist