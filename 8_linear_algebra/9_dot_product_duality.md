


# Dot Product

## 1. What is the Dot Product?

The **dot product** is an operation that takes two vectors and produces a **scalar (single number)**.

For two vectors:

$$
\mathbf{a} = [a_1, a_2, ..., a_n]
$$

$$
\mathbf{b} = [b_1, b_2, ..., b_n]
$$

The dot product is:

$$
\mathbf{a} \cdot \mathbf{b}
=
a_1b_1 + a_2b_2 + ... + a_nb_n
$$

---

## 2. Example

$$
\mathbf{a} = [2, 3]
$$

$$
\mathbf{b} = [4, 5]
$$

$$
\mathbf{a} \cdot \mathbf{b}
=
(2)(4) + (3)(5)
$$

$$
= 8 + 15 = 23
$$

The result is:

$$
\boxed{23}
$$

Notice that the result is a scalar, not a vector.

---

## 3. Dot Product Using Matrices

A row vector multiplied by a column vector:

$$
\mathbf{a}^T\mathbf{b}
$$

Example:

$$
\begin{bmatrix}
2 & 3
\end{bmatrix}
\begin{bmatrix}
4 \\
5
\end{bmatrix}
=
2(4) + 3(5)
=
23
$$

---

## 4. Geometric Meaning

The dot product is:

$$
\mathbf{a} \cdot \mathbf{b}
=
\|\mathbf{a}\|
\|\mathbf{b}\|
\cos(\theta)
$$

Where:

- $\|\mathbf{a}\|$ = length of vector $\mathbf{a}$
- $\|\mathbf{b}\|$ = length of vector $\mathbf{b}$
- $\theta$ = angle between the vectors

---

## 5. Understanding the Sign

### Positive Dot Product

If:

$$
\mathbf{a} \cdot \mathbf{b} > 0
$$

The angle between the vectors is less than $90^\circ$.

The vectors point generally in similar directions.

---

### Zero Dot Product

If:

$$
\mathbf{a} \cdot \mathbf{b} = 0
$$

Then:

$$
\cos(90^\circ) = 0
$$

The vectors are **orthogonal (perpendicular)**.

---

### Negative Dot Product

If:

$$
\mathbf{a} \cdot \mathbf{b} < 0
$$

The angle is greater than $90^\circ$.

The vectors point generally in opposite directions.

---

## 6. Vector Norm / Length

The length of a vector is called its **norm**.

For:

$$
\mathbf{a} = [a_1, a_2, ..., a_n]
$$

The Euclidean norm is:

$$
\|\mathbf{a}\|
=
\sqrt{a_1^2 + a_2^2 + ... + a_n^2}
$$

Example:

$$
\mathbf{a} = [3, 4]
$$

$$
\|\mathbf{a}\|
=
\sqrt{3^2 + 4^2}
=
\sqrt{25}
=
5
$$

---

## 7. Cosine Similarity

The dot product can be used to measure the similarity between vectors.

$$
\cos(\theta)
=
\frac{\mathbf{a} \cdot \mathbf{b}}
{\|\mathbf{a}\|\|\mathbf{b}\|}
$$

This is called **cosine similarity**.

It is commonly used in:

- Machine Learning
- Natural Language Processing
- Recommendation Systems
- Word Embeddings
- Vector Databases

---

## 8. Dot Product in Machine Learning

Suppose:

$$
\mathbf{x} = [x_1, x_2, x_3]
$$

and:

$$
\mathbf{w} = [w_1, w_2, w_3]
$$

A linear model can calculate:

$$
\mathbf{w} \cdot \mathbf{x}
$$

$$
=
w_1x_1 + w_2x_2 + w_3x_3
$$

This is the foundation of:

- Linear Regression
- Logistic Regression
- Neural Networks

---

## Key Idea

The dot product combines:

1. The size of two vectors
2. Their directional relationship

It answers:

> How much does one vector point in the direction of another?

