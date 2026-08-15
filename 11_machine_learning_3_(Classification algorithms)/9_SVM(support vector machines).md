Support Vector Machine (SVM)
1. Introduction

SVM = Support Vector Machine

SVM is a supervised machine learning algorithm mainly used for:

Classification
Regression
Finding a separating decision boundary

The main idea behind SVM is:

Find the decision boundary that separates classes while maximizing the margin between the classes.

SVM is especially known for:

Hyperplane
Margin
Support Vectors
Decision Function
Kernel Trick for non-linear data
2. Basic Idea

Suppose we have two classes:

Class 0 → 🔵
Class 1 → 🔴

A dataset might look like:

🔵 🔵 🔵

   🔵

       🔵

          🔴

             🔴

                🔴 🔴

SVM tries to find a boundary between the two classes:

🔵 🔵 🔵

   🔵

       🔵

---------- Decision Boundary ----------

          🔴

             🔴

                🔴 🔴

But there can be many possible boundaries.

SVM tries to find the best boundary.

The best boundary is generally the one that provides the maximum margin.

3. Hyperplane

A hyperplane is the decision boundary used by SVM.

The meaning depends on the number of dimensions.

2 Dimensions

With two features:

x₁
│
│        🔵
│     🔵
│
│
│------------- Decision Boundary
│
│          🔴
│       🔴
│
└──────────────── x₂

The hyperplane is a line.

So:

2D → hyperplane = line

Example:

[
w_1x_1+w_2x_2+b=0
]

4. Hyperplane in 3 Dimensions

If we have three features:

x₁
x₂
x₃

the decision boundary is no longer a line.

It becomes a plane.

3 features
      ↓
Hyperplane = Plane

The equation becomes:

[
w_1x_1+w_2x_2+w_3x_3+b=0
]

5. Hyperplane in N Dimensions

Suppose we have n features:

x₁, x₂, x₃, ..., xₙ

The SVM hyperplane is:

[
w_1x_1+w_2x_2+w_3x_3+\cdots+w_nx_n+b=0
]

Using vector notation:

[
\boxed{\mathbf{w}^T\mathbf{x}+b=0}
]

where:

x = feature vector
w = weight vector
b = bias/intercept
wᵀx = dot product
Important correction

A hyperplane is not a "best-fit vector."

Instead:

The weight vector w is perpendicular (normal) to the hyperplane.

So:

w → normal/weight vector
          ↓
          │
          │
----------┼----------  ← Hyperplane

The vector w tells us the orientation of the hyperplane.

6. The Equation wx + b = 0

The fundamental SVM equation is:

[
\boxed{\mathbf{w}^T\mathbf{x}+b=0}
]

For 2D:

[
w_1x_1+w_2x_2+b=0
]

We can rearrange:

[
w_2x_2=-w_1x_1-b
]

[
x_2=-\frac{w_1}{w_2}x_1-\frac{b}{w_2}
]

This looks like:

[
y=mx+c
]

So in 2D, the SVM decision boundary is simply a line.

7. What Does w Mean?

Suppose:

[
w=
\begin{bmatrix}
w_1\
w_2
\end{bmatrix}
]

Then:

[
w^Tx=w_1x_1+w_2x_2
]

The vector w determines the orientation of the decision boundary.

Most importantly:

w is perpendicular to the hyperplane.

8. What Does b Mean?

b is the bias/intercept.

It controls the position of the hyperplane.

For example:

[
w^Tx+b=0
]

Changing b moves the boundary.

Conceptually:

b changes
   ↓
Position of boundary changes

while w mainly controls:

w changes
   ↓
Orientation of boundary changes
9. Prediction Using wx + b

SVM uses the value:

[
f(x)=w^Tx+b
]

This value tells us which side of the hyperplane the point is on.

The decision boundary occurs when:

[
w^Tx+b=0
]

Therefore:

wᵀx + b > 0
        ↓
     Class +1

and:

wᵀx + b < 0
        ↓
     Class -1

while:

wᵀx + b = 0
        ↓
Decision Boundary
10. Example Prediction

Suppose:

[
w=
\begin{bmatrix}
2\
3
\end{bmatrix}
]

and:

[
b=-5
]

Our point is:

[
x=
\begin{bmatrix}
2\
1
\end{bmatrix}
]

Calculate:

[
w^Tx+b
]

[
=(2)(2)+(3)(1)-5
]

[
=4+3-5
]

[
=2
]

Since:

[
2>0
]

the point belongs to:

Class +1
11. Decision Function

The SVM decision function can be written as:

[
\boxed{f(x)=w^Tx+b}
]

Classification:

[
\hat y=
\begin{cases}
+1 & \text{if } w^Tx+b>0\
-1 & \text{if } w^Tx+b<0
\end{cases}
]

The boundary is:

[
\boxed{w^Tx+b=0}
]

12. Margin

Finding a separating line is not enough.

SVM wants to find a boundary that has the largest possible margin.

The margin is the distance between the decision boundary and the closest data points.

Conceptually:

Class +1

🔵 🔵

   🔵 ← Support Vector

       | ← Margin
       |
-------|------- Decision Boundary
       |
       | ← Margin

   🔴 ← Support Vector

🔴 🔴

The larger the margin, the better separated the classes are considered to be.

13. Margin Lines

SVM has three important lines/hyperplanes:

1. Positive margin

[
w^Tx+b=1
]

2. Decision boundary

[
\boxed{w^Tx+b=0}
]

3. Negative margin

[
w^Tx+b=-1
]

Conceptually:

        wᵀx + b = +1
-----------------------------  ← Margin boundary


        wᵀx + b = 0
-----------------------------  ← Decision Boundary


        wᵀx + b = -1
-----------------------------  ← Margin boundary

The two outer boundaries define the margin.

14. Support Vectors

The data points closest to the decision boundary are called:

Support Vectors

Example:

🔵 🔵 🔵

      🔵  ← Support Vector

          |
          |
----------|----------  ← Decision Boundary
          |
      🔴  ← Support Vector

🔴 🔴 🔴

The support vectors are extremely important because they determine the position of the optimal boundary.

15. Why Are They Called Support Vectors?

Imagine the decision boundary is being "supported" by the closest points.

🔵                 🔴
      🔵       🔴
         \     /
          \   /
       Boundary

The closest points constrain where the boundary can be placed.

Therefore:

Support vectors are the training samples closest to the decision boundary that determine the optimal separating hyperplane.

16. Margin Width

For the canonical SVM formulation:

[
w^Tx+b=1
]

and:

[
w^Tx+b=-1
]

the total margin width is:

[
\boxed{\frac{2}{|w|}}
]

Therefore:

[
\text{Margin} \propto \frac{1}{|w|}
]

To maximize the margin, SVM tries to minimize:

[
|w|
]

or, more conveniently:

[
\frac{1}{2}|w|^2
]

17. Why Does SVM Want Maximum Margin?

Imagine two possible boundaries.

Boundary A
🔵 🔵   | 🔴
🔵      |   🔴

Very close to the data.

Boundary B
🔵 🔵       |       🔴
🔵          |          🔴

There is more space between the boundary and the closest points.

SVM prefers:

Maximum Margin
       ↓
Better separation
       ↓
Better generalization

The idea is that a larger margin can make the classifier less sensitive to small changes in the data.

18. Hard Margin SVM

If the data is perfectly linearly separable, we can require:

[
y_i(w^Tx_i+b)\geq1
]

for every training example.

This is called the hard-margin case.

Conceptually:

🔵 🔵 🔵

   🔵

-----------------

   margin

-----------------

   🔴

🔴 🔴 🔴

No training point is allowed inside the margin or on the wrong side.

19. Soft Margin SVM

Real-world data is often not perfectly separable.

Example:

🔵 🔵

   🔵 🔴

      🔴

🔴 🔵

SVM can allow some violations.

This is called:

Soft Margin SVM

Slack variables are introduced:

[
y_i(w^Tx_i+b)\geq1-\xi_i
]

where:

[
\xi_i\geq0
]

The ξ values allow points to violate the ideal margin.

20. The C Parameter

The C parameter controls how strongly SVM penalizes margin violations.

Small C
Small C
   ↓
More tolerance for violations
   ↓
Wider margin
Large C
Large C
   ↓
Strong penalty for violations
   ↓
Tries harder to classify training points correctly
   ↓
Can produce a narrower margin

Simplified:

Small C → wider margin + more mistakes allowed

Large C → narrower margin + fewer training mistakes
21. Linear SVM Visualization

For a 2D classification problem:

Feature 2
   ↑

   🔵 🔵
      🔵

      🔵  ← Support Vector

   +1  ------------------  Margin

   0   ------------------  Decision Boundary

   -1  ------------------  Margin

      🔴  ← Support Vector
         🔴
   🔴 🔴

   └──────────────────────→ Feature 1

The three important equations are:

[
w^Tx+b=1
]

[
w^Tx+b=0
]

[
w^Tx+b=-1
]

22. Distance From a Point to the Hyperplane

For a point x, the signed distance from the hyperplane is proportional to:

[
w^Tx+b
]

The actual perpendicular distance is:

[
\boxed{
\frac{|w^Tx+b|}{|w|}
}
]

This explains why the norm of w matters when calculating the margin.

23. Complete SVM Mental Model

Think about SVM in this order:

                    DATA
                      ↓
              Two or more classes
                      ↓
              Find a boundary
                      ↓
                Hyperplane
                      ↓
       ┌──────────────┴──────────────┐
       ↓                             ↓
   Class +1                       Class -1
       ↓                             ↓
       └──────────┬──────────────────┘
                  ↓
            Find closest points
                  ↓
           Support Vectors
                  ↓
           Create maximum margin
                  ↓
           Optimal Hyperplane
                  ↓
              Prediction
                  ↓
             wᵀx + b
                  ↓
        ┌─────────┴─────────┐
        ↓                   ↓
      > 0                  < 0
        ↓                   ↓
     Class +1            Class -1
24. Important Terminology
Term	Meaning
SVM	Support Vector Machine
Hyperplane	Decision boundary in feature space
Weight vector w	Determines orientation of hyperplane
Bias b	Controls position of hyperplane
Decision boundary	wᵀx + b = 0
Margin	Distance between boundary and closest points
Support vectors	Closest important training points
Margin boundaries	wᵀx+b = ±1
C	Controls penalty for margin violations
Kernel	Allows non-linear decision boundaries
25. 2D vs 3D vs N-D
Number of Features       Decision Boundary

2 features               Line

3 features               Plane

N features               Hyperplane

Mathematically:

[
\boxed{w_1x_1+w_2x_2+\cdots+w_nx_n+b=0}
]

or:

[
\boxed{w^Tx+b=0}
]

26. SVM vs "Best Fit Line"

Be careful with this terminology.

In Linear Regression:

Find the line that best fits
the numerical target values.

In SVM classification:

Find a separating hyperplane
with maximum margin.

Therefore, don't think:

"SVM finds the best-fit line."

A better statement is:

SVM finds an optimal separating hyperplane that maximizes the margin between classes.

27. Final Mental Picture
                  🔵 🔵 🔵

                     🔵

              🔵 ← SUPPORT VECTOR

              +1 ─────────────────
                    ↑
                    │
                    │ MARGIN
                    │
              0  ───┼─────────────────
                    │
                    │ MARGIN
                    │
              -1 ─────────────────
              
              🔴 ← SUPPORT VECTOR

                  🔴 🔴 🔴

The core equations:

[
\boxed{w^Tx+b=0}
]

→ Decision boundary

[
\boxed{w^Tx+b=\pm1}
]

→ Margin boundaries

[
\boxed{\text{Margin}=\frac{2}{|w|}}
]

→ Total margin width

[
\boxed{
\hat y=
\begin{cases}
+1,&w^Tx+b>0\
-1,&w^Tx+b<0
\end{cases}}
]

→ Prediction

🧠 SVM in One Sentence

SVM finds a hyperplane wᵀx+b=0 that separates classes while maximizing the margin, where the closest training points are the support vectors, and predictions are made according to which side of the hyperplane a point lies on.