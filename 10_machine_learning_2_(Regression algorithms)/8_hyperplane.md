# Hyperplane - Short Notes

## Definition
A **hyperplane** is a subspace of one dimension less than its ambient space.  
In an \( n \)-dimensional space, a hyperplane has dimension \( n-1 \).

## Mathematical Representation
In \(\mathbb{R}^n\), a hyperplane is defined by the linear equation:

\[
w \cdot x + b = 0
\]

where:
- \( w \) = normal vector (perpendicular to the hyperplane)
- \( b \) = bias/intercept term
- \( x \) = point on the hyperplane

## Key Properties
- **Divides space**: Splits the space into two **half-spaces**:
  - \( w \cdot x + b > 0 \)
  - \( w \cdot x + b < 0 \)
- **Decision boundary**: Used in SVMs, perceptrons, and linear classifiers.
- **Normal vector**: \( w \) defines the orientation of the hyperplane.

## Distance from a Point
The perpendicular distance from a point \( x_0 \) to the hyperplane is:

\[
d = \frac{|w \cdot x_0 + b|}{\|w\|}
\]

## Special Cases
| Dimension | Hyperplane |
|-----------|------------|
| 1D line   | Point (0D) |
| 2D plane  | Line (1D)  |
| 3D space  | Plane (2D) |

## Applications
- Support Vector Machines (SVMs)
- Neural network decision boundaries
- Linear regression and classification
- Geometry and optimization

## Summary
> A hyperplane is a flat, affine subspace that separates a space into two regions. It is fundamental in machine learning for classification and geometry.

## Quick Formula Card
- **Equation:** \( w \cdot x + b = 0 \)
- **Distance:** \( \frac{|w \cdot x_0 + b|}{\|w\|} \)
- **Dimension:** \( n-1 \) in \( n \)-dimensional space