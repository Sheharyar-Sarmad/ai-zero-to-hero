# Matrix Multiplication as Composition

## 1. Main Idea

Matrix multiplication can be understood as the **composition of linear transformations**.

A matrix represents a transformation that takes an input vector and produces an output vector.

For example:

```text
v → Bv → A(Bv)

This means:

First apply matrix B to vector v.
Then apply matrix A to the result.
The complete transformation is represented by AB.

Therefore:

ABv = A(Bv)

So:

AB = A ∘ B

The matrix on the right acts first.

2. Function Composition Analogy

For ordinary functions:

f(g(x))

The function g is applied first, and then f is applied to the result.

The same idea applies to matrices:

ABv = A(Bv)

The matrix B is applied first, and then matrix A.

Important Rule
AB means:

First apply B
Then apply A

The rightmost matrix acts first.

3. Example

Suppose:

B = | 2  0 |
    | 0  1 |

This matrix stretches the x-coordinate by 2.

And:

A = | 1  0 |
    | 0  3 |

This matrix stretches the y-coordinate by 3.

Let:

v = | 1 |
    | 1 |
Step 1: Apply Matrix B
Bv = | 2  0 | | 1 |
     | 0  1 | | 1 |

Therefore:

Bv = | 2 |
     | 1 |

The vector has now been transformed by B.

Step 2: Apply Matrix A

Now apply A to the result:

A(Bv) = | 1  0 | | 2 |
        | 0  3 | | 1 |

Therefore:

A(Bv) = | 2 |
        | 3 |

So:

ABv = | 2 |
      | 3 |

The complete transformation is:

v → Bv → A(Bv)
4. Multiplying the Matrices First

Instead of applying the transformations one by one, we can multiply the matrices first.

AB = | 1  0 | | 2  0 |
     | 0  3 | | 0  1 |

The result is:

AB = | 2  0 |
     | 0  3 |

Now apply the combined matrix to v:

ABv = | 2  0 | | 1 |
      | 0  3 | | 1 |

Therefore:

ABv = | 2 |
      | 3 |

This is the same result as applying the transformations separately.

Therefore:

A(Bv) = (AB)v

This is the fundamental idea of matrix composition.

5. Matrix Multiplication Combines Transformations

Suppose:

T₁(v) = Av

and:

T₂(v) = Bv

If we apply T₂ first and then T₁:

T₁(T₂(v)) = A(Bv)

Using matrix multiplication:

A(Bv) = (AB)v

Therefore, the combined transformation is:

AB
In Simple Words

Matrix multiplication creates a new transformation by combining two existing transformations.

Instead of performing:

v → Bv → A(Bv)

we can create one matrix:

AB

and directly perform:

v → ABv
6. Matrix Multiplication Is Not Commutative

Matrix multiplication is generally not commutative.

This means:

AB ≠ BA

Usually:

A(Bv) ≠ B(Av)

This happens because applying transformations in different orders can produce different results.

For example:

Transformation Order 1
1. Rotate a vector
2. Then stretch it
Transformation Order 2
1. Stretch a vector
2. Then rotate it

These two processes can produce different final results.

Therefore:

AB ≠ BA

in many cases.

Important

The order of matrix multiplication matters because the order of transformations matters.

7. Why Does the Right Matrix Act First?

Consider:

ABv

Matrix multiplication is evaluated from the right:

ABv = A(Bv)

First:

Bv

Then:

A(Bv)

Therefore, the transformation order is:

v → B → A

Not:

v → A → B

This is one of the most important ideas in linear algebra.

Visual Representation
Input Vector
     │
     ▼
     v
     │
     ▼
 Matrix B
     │
     ▼
    Bv
     │
     ▼
 Matrix A
     │
     ▼
   A(Bv)

The complete transformation is:

ABv
8. Composition of Functions vs Matrices
Function Composition	Matrix Composition
f(g(x))	A(Bv)
g acts first	B acts first
f acts second	A acts second
f ∘ g	A ∘ B
Combined function	Product matrix AB

The key relationship is:

ABv = A(Bv)

This means matrix multiplication behaves like function composition.

9. Geometric Interpretation

A matrix can transform space in many ways.

Common linear transformations include:

Scaling
Rotation
Reflection
Shearing
Projection

When matrices are multiplied, their transformations are composed.

For example:

Vector
   │
   ▼
Rotation Matrix R
   │
   ▼
Rotated Vector
   │
   ▼
Scaling Matrix S
   │
   ▼
Final Vector

The combined transformation is:

SR

because:

SRv = S(Rv)

The order is:

v → Rv → S(Rv)

Therefore:

R acts first.
S acts second.

The rightmost matrix acts first.

10. Important Formula

For two matrices A and B:

(AB)v = A(Bv)

This means:

Matrix Multiplication = Composition of Linear Transformations

In mathematical notation:

AB = A ∘ B

where:

B acts first
A acts second
11. Connection to the Matrix Multiplication Rule

The entry of a matrix product is calculated using the row-column dot product:

(AB)ᵢⱼ = Σₖ aᵢₖbₖⱼ

This rule is not arbitrary.

It is specifically designed so that matrix multiplication correctly represents the composition of transformations.

The fundamental property is:

A(Bv) = (AB)v

This property allows us to replace two consecutive transformations:

v → Bv → A(Bv)

with one combined transformation:

v → ABv
12. The Main Concept

Suppose:

T₁(v) = Av

and:

T₂(v) = Bv

Then:

T₁ ∘ T₂

means:

First apply T₂
Then apply T₁

In matrix form:

A ∘ B = AB

Therefore:

(AB)v = A(Bv)

The matrix product AB represents the composition of the two transformations.

13. Key Takeaways
1. A matrix represents a transformation
v → Av
2. Matrix multiplication combines transformations
v → Bv → A(Bv)

can be written as:

v → ABv
3. The rightmost matrix acts first
ABv = A(Bv)

The order is:

v → B → A
4. Matrix multiplication is generally not commutative
AB ≠ BA

because:

A(Bv) ≠ B(Av)

in general.

5. Matrix multiplication is associative

Matrix multiplication satisfies:

(AB)C = A(BC)

This means that when applying several transformations, the grouping can change, but the order of the transformations remains the same.

For example:

(AB)Cv = AB(Cv)

The transformations are still applied in the order:

v → C → B → A
14. Final Summary

A matrix represents a transformation.

When two transformations are applied one after another:

v → Bv → A(Bv)

they can be combined into a single matrix:

AB

Therefore:

ABv = A(Bv)

The most important rule is:

AB

The matrix on the right acts first:

B acts first
A acts second

So:

v → B → A

Matrix multiplication is therefore not just a numerical calculation.

Matrix multiplication is a way to combine linear transformations into one transformation.


This version is ready to save as:

```text
matrix-multiplication-as-composition.md8w