


# K-Means Clustering

K-Means is an **unsupervised learning algorithm** used to divide data into groups called **clusters**.

The main idea is simple:

> Put similar data points together and represent each group using a center point called a **centroid**.

---

## 1. What does K mean?

`K` is simply the **number of clusters** we want.

For example:

```text
K = 3
```

means we want the algorithm to find **3 clusters**.

```text
Cluster 1 → Centroid 1
Cluster 2 → Centroid 2
Cluster 3 → Centroid 3
```

The important question is: **How do we know what K should be?**

One common method is the **Elbow Method**, which we'll see later.

---

## 2. Initializing Centroids

Before K-Means can start grouping the data, it needs some starting **centroids**.

If:

```text
K = 3
```

then we need 3 initial centroids:

```text
C₁
C₂
C₃
```

These are basically **initial guesses for the centers of the clusters**.

A common initialization method is **K-Means++**, which tries to choose better starting positions instead of simply picking random points.

---

## 3. Euclidean Distance

K-Means needs a way to determine which centroid is closest to a data point.

It uses **Euclidean distance**.

For two points:

```text
P = (x₁, y₁)
C = (x₂, y₂)
```

the Euclidean distance is:

[
d = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}
]

### Example

Suppose:

```text
Point     = (2, 3)
Centroid  = (5, 7)
```

Then:

[
d = \sqrt{(2-5)^2 + (3-7)^2}
]

[
= \sqrt{(-3)^2 + (-4)^2}
]

[
= \sqrt{9+16}
]

[
= \sqrt{25}
]

[
= 5
]

So the point is **5 units away** from the centroid.

---

## 4. Assigning Points to Centroids

K-Means calculates the distance from **every data point to every centroid**.

For example, suppose we have:

```text
K = 3
```

For point `P₁`:

```text
P₁ → C₁ = 2.4
P₁ → C₂ = 7.1
P₁ → C₃ = 4.8
```

The smallest distance is:

```text
2.4 → C₁
```

So:

```text
P₁ belongs to Cluster 1
```

The same thing happens for **every data point**.

So if we have 500 points and K = 3, K-Means calculates the distance of each point to all 3 centroids.

---

## 5. Reassigning Points

After calculating the distances, every point is assigned to its **nearest centroid**.

For example:

```text
P₁ → C₁
P₂ → C₃
P₃ → C₁
P₄ → C₂
P₅ → C₂
```

This gives us:

```text
Cluster 1 → P₁, P₃
Cluster 2 → P₄, P₅
Cluster 3 → P₂
```

These assignments can change later when the centroids move.

---

## 6. Moving the Centroids

Now K-Means looks at the points inside each cluster and calculates their **mean position**.

That mean becomes the new centroid.

For example, suppose Cluster 1 contains:

```text
(2, 4)
(4, 6)
(6, 8)
```

Calculate the average X:

[
x = \frac{2+4+6}{3}=4
]

Calculate the average Y:

[
y = \frac{4+6+8}{3}=6
]

So the new centroid is:

```text
C₁ = (4, 6)
```

The centroid has now **moved** to the average position of its assigned points.

---

## 7. K-Means Repeats

This process keeps happening:

```text
Choose K
   ↓
Initialize centroids
   ↓
Calculate distances
   ↓
Assign each point to nearest centroid
   ↓
Calculate new centroids
   ↓
Move centroids
   ↓
Calculate distances again
   ↓
Reassign points
   ↓
Repeat...
```

Eventually, the centroids and assignments stop changing significantly.

That's when K-Means has **converged**.

---

# WCSS — Within-Cluster Sum of Squares

## 8. What is WCSS?

**WCSS** stands for:

> **Within-Cluster Sum of Squares**

It tells us how spread out the points are **inside their clusters**.

In simple terms:

> How far are our data points from the centroid of their cluster?

For every point, we calculate its distance from its assigned centroid, **square that distance**, and add all of them together.

For one cluster:

[
WCSS = d_1^2 + d_2^2 + d_3^2 + \cdots + d_n^2
]

For example, if the distances are:

```text
2, 3, 5
```

then:

[
WCSS = 2^2 + 3^2 + 5^2
]

[
= 4 + 9 + 25
]

[
= 38
]

For all clusters, we add the WCSS of every cluster together.

---

## 9. WCSS Formula

The general formula is:

[
WCSS =
\sum_{k=1}^{K}
\sum_{x_i \in C_k}
|x_i-\mu_k|^2
]

Where:

* `K` = number of clusters
* `Cₖ` = cluster `k`
* `xᵢ` = a data point
* `μₖ` = centroid of cluster `k`
* `||xᵢ - μₖ||²` = squared Euclidean distance from the point to its centroid

So basically:

```text
WCSS =
distance² of point 1
+ distance² of point 2
+ distance² of point 3
+ ...
+ distance² of all points
```

### Think of WCSS as the total "spread/error" inside all clusters.

```text
Small WCSS
     ↓
Points are closer to their centroids
     ↓
Clusters are more compact
```

K-Means tries to **minimize WCSS**.

---

## 10. Why Do We Square the Distance?

We square the distances because K-Means is based on **squared Euclidean distance**.

For example:

```text
Distance = 2  →  2² = 4
Distance = 5  →  5² = 25
```

Notice that the larger distance gets penalized much more.

This means points that are very far from their centroid contribute heavily to WCSS.

---

# Elbow Method

## 11. Why Do We Need the Elbow Method?

We know K-Means needs us to choose `K`.

But how do we know whether:

```text
K = 2
K = 3
K = 4
K = 5
```

is the right choice?

We can calculate WCSS for different values of K and look at how it changes.

---

## 12. Elbow Method

We train K-Means multiple times:

```text
K = 1 → calculate WCSS
K = 2 → calculate WCSS
K = 3 → calculate WCSS
K = 4 → calculate WCSS
K = 5 → calculate WCSS
...
```

Example:

| Number of Clusters (K) | WCSS |
| ---------------------: | ---: |
|                      1 | 1000 |
|                      2 |  600 |
|                      3 |  350 |
|                      4 |  300 |
|                      5 |  270 |
|                      6 |  250 |

Then we plot:

WCSS
 │
 │ ●
 │  \
 │   \
 │    ●
 │     \
 │      ●
 │       \
 │        ●──●──●
 │
 └────────────────── K
   1   2   3   4  5  6
```

---

## 13. Elbow Curve

The graph of:

K vs WCSS

is called the **Elbow Curve**.

As K increases, WCSS decreases because we're adding more centroids.

For example:

K = 1 → WCSS = 1000
K = 2 → WCSS = 600
K = 3 → WCSS = 350
K = 4 → WCSS = 300
K = 5 → WCSS = 270

Notice the improvement:

1 → 2   huge improvement
2 → 3   huge improvement
3 → 4   small improvement
4 → 5   small improvement

The point where the improvement starts becoming much smaller is the **elbow**.

If the elbow is around:

K = 3

we may choose:

K = 3

---

## 14. Why Does WCSS Decrease When K Increases?

Imagine we have:

```text
K = 1
```

All data points have to use **one centroid**.

Some points may be very far from it.

Now:

```text
K = 2
```

We have two centroids, so points can be closer to their assigned centroid.

Then:

```text
K = 3
```

we have even more flexibility.

So generally:

```text
More K
   ↓
More centroids
   ↓
Points can be closer to a centroid
   ↓
Lower WCSS
```

This is why **WCSS normally keeps decreasing as K increases**.

---

## 15. Why Not Just Choose a Very Large K?

Because if we keep increasing K, eventually every point could have its own cluster.

For example:

```text
100 data points
K = 100
```

Each point could have its own centroid.

Then WCSS can become:

```text
0
```

But that's not useful clustering.

We don't want the **lowest possible WCSS**.

We want a **reasonable number of clusters** that gives a good balance between:

* compact clusters
* reasonable number of clusters

That's the purpose of the **Elbow Method**.

---

# Main Objective of K-Means

The mathematical objective of K-Means is:

[
\min
\sum_{k=1}^{K}
\sum_{x_i \in C_k}
|x_i-\mu_k|^2
]

In plain English:

> **Find K clusters and their centroids so that the total squared distance between every point and the centroid of its cluster is as small as possible.**

---

# Complete Mental Model

Think of K-Means like this:

```text
                    Choose K
                       ↓
                Initialize centroids
                       ↓
          Calculate distance to each centroid
                       ↓
             Choose nearest centroid
                       ↓
                Create clusters
                       ↓
             Calculate cluster means
                       ↓
               Move the centroids
                       ↓
                  Repeat again
                       ↓
             Centroids stabilize
```

Then, when choosing `K` beforehand is difficult:

```text
Try K = 1, 2, 3, 4, 5...
            ↓
      Calculate WCSS
            ↓
      Plot K vs WCSS
            ↓
       Find the "elbow"
            ↓
        Choose a K
```

---

## Quick Revision

| Term                   | Meaning                                             |
| ---------------------- | --------------------------------------------------- |
| **K**                  | Number of clusters                                  |
| **Cluster**            | Group of similar data points                        |
| **Centroid**           | Mean/center of a cluster                            |
| **Initialization**     | Choosing the starting centroids                     |
| **Euclidean Distance** | Straight-line distance between a point and centroid |
| **Assignment**         | Giving a point to its nearest centroid              |
| **Recalculation**      | Finding the new mean of each cluster                |
| **WCSS**               | Sum of squared distances within all clusters        |
| **Elbow Method**       | Method used to help choose K                        |
| **Elbow Curve**        | Graph of K against WCSS                             |
| **Goal**               | Minimize WCSS without unnecessarily increasing K    |

### One-line definition

> **K-Means repeatedly assigns each data point to its nearest centroid and then moves each centroid to the mean of its assigned points, with the goal of minimizing within-cluster squared distances (WCSS).**
