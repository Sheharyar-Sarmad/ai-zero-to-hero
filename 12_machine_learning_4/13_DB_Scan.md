# DBSCAN Algorithm - Complete Notes

## What is DBSCAN?

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that groups together points that are closely packed together, marking points in low-density regions as outliers.

---

## Why DBSCAN? (The K-Means Problem)

### What's wrong with K-Means?

K-Means fails badly when:

- **Non-spherical clusters** - Can't handle moon-shaped or ring-shaped data
- **Different cluster sizes** - Forces equal-sized clusters
- **Different densities** - Can't handle varying point densities
- **Requires K** - You must pre-define number of clusters
- **Outlier sensitive** - Outliers pull centroids away

### Real-world example:

Imagine customer data with:

- **High-density cluster**: Regular buyers in a city
- **Low-density cluster**: Premium buyers spread across suburbs
- **Outliers**: One-time buyers

**K-Means** would split regular buyers into multiple groups [X]  
**DBSCAN** finds both clusters naturally [✓]

---

## What is Epsilon (ε) Distance?

### The 1-Unit Epsilon Concept

Think of **ε** as the radius of a circle drawn around each point.

1 Unit Epsilon = The "Friendship Radius"

If you have 5 friends (MinPts) within this 1-unit circle → You're a Core Point

If you have fewer friends → You're either Border or Noise

text

### Visual Representation:
[ε = 1 unit]

Imagine a circle with radius 1:

 ╭──────────╮
/ ● \ ← Point A (Core)
| ╭───╮ |
| │ ● │ ● | ← Points B & C (within ε distance)
| ╰───╯ |
\ ● / ← Point D (also within ε)
 ╰──────────╯
↑
This entire area
has radius = 1 unit

text

### Proportion Mapping:

- **0.5ε**: Half the radius → Very dense neighborhood
- **1.0ε**: Full radius → Standard checking distance
- **2.0ε**: Double radius → Too far, not considered neighbors

---

## DBSCAN Parameters

### 1. Epsilon (ε) - The Distance Threshold

| Aspect | Description |
|--------|-------------|
| **What it is** | Maximum distance between two points to be considered neighbors |
| **How to choose** | Use K-distance plot (elbow method) |
| **Rule of thumb** | Small ε → Many clusters with noise \| Large ε → Fewer clusters |

### 2. MinPts - Minimum Points

| Aspect | Description |
|--------|-------------|
| **What it is** | Minimum number of points required to form a dense region |
| **Default** | MinPts ≥ D+1 (where D = dimensions) |
| **Common value** | 4 for 2D data, 10 for higher dimensions |
| **Rule** | Higher MinPts → Less sensitive to noise |

---

## Point Classifications
┌─────────────────────────────────────────────────────────────┐
│ │
│ 1. CORE POINT │
│ - Has ≥ MinPts points within ε radius │
│ - Forms the backbone of clusters │
│ - Expands the cluster │
│ │
│ 2. BORDER POINT │
│ - Has < MinPts points within ε radius │
│ - But is within ε of a Core Point │
│ - Lies on the edge of cluster │
│ │
│ 3. NOISE POINT │
│ - Has < MinPts points within ε radius │
│ - NOT within ε of any Core Point │
│ - Considered as outlier │
│ │
└─────────────────────────────────────────────────────────────┘

text

---

## How DBSCAN Works (Step-by-Step)

### Step 1: Scan & Classify
For each point P in dataset:
Count points within ε distance
If count ≥ MinPts:
Label P as CORE POINT
Else:
Label P as NON-CORE

text

### Step 2: Build Clusters
For each unvisited Core Point:
Create new cluster
Add all core points within ε distance
Add all border points within ε distance
Expand: Check neighbors' neighbors
Stop when no more density-reachable points

text

### Step 3: Assign Noise
Any remaining unvisited points = NOISE

text

### Density-Reachability Rule:
If P is Core and Q is within ε of P:
Then Q is density-reachable from P

text

---

## Advantages & Disadvantages

### Advantages

| Feature | Benefit |
|---------|---------|
| **No K needed** | Automatically finds number of clusters |
| **Arbitrary shapes** | Handles non-spherical clusters |
| **Robust to outliers** | Identifies noise points separately |
| **Parameters intuitive** | ε and MinPts make physical sense |
| **Works with spatial data** | Perfect for GIS, GPS tracking |

### Disadvantages

| Issue | Challenge |
|-------|-----------|
| **Parameter sensitivity** | Wrong ε/MinPts = bad clusters |
| **Varying densities** | Single ε doesn't work for all densities |
| **High dimensions** | Curse of dimensionality breaks distance |
| **Computational cost** | O(n²) time complexity |
| **Non-deterministic** | Order of points can affect results |

---

## Real-World Applications

### GPS Navigation
- Find traffic congestion zones (dense vehicle clusters)
- Identify accident hotspots

### Social Networks
- Find friend circles based on interactions
- Detect bot accounts (isolated noise)

### Healthcare
- Cluster disease outbreaks by location
- Identify abnormal patient vitals

### E-commerce
- Group customers by purchase behavior
- Detect fraudulent transactions

### Astronomy
- Find star clusters in galaxies
- Identify cosmic anomalies

---

## Quick Decision Guide
┌─────────────┐
│ Your Data │
└──────┬──────┘
│
▼
┌─────────────────────────────┐
│ Is it SPHERICAL/shape │ YES → Use K-Means
│ and you know K? │
└─────────────────────────────┘
│ NO
▼
┌─────────────────────────────┐
│ Is it IRREGULAR shape │ YES → Use DBSCAN
│ with DENSE regions? │
└─────────────────────────────┘
│ NO
▼
┌─────────────────────────────┐
│ Try Hierarchical or │
│ Spectral Clustering │
└─────────────────────────────┘

text

---

## Parameter Tuning Tips

### To Find Good ε:

1. Calculate distance to k-nearest neighbor (k = MinPts)
2. Sort distances ascending
3. Plot the K-distance graph
4. Find the "elbow" point
5. Use that distance as ε

### To Choose MinPts:

- **Small dataset**: Use 3-5
- **Large dataset**: Use 10-20
- **Rule of thumb**: At least D+1
- **Domain knowledge**: Based on expected cluster size

---

## Summary Cheat Sheet
DBSCAN = Density + Reachability

CLUSTER = Core Points + Border Points
NOISE = Points not in any cluster

CORE → Has ≥ MinPts neighbors within ε
BORDER → Has < MinPts neighbors but near Core
NOISE → Isolated, far from any Core

ε (epsilon) = Your "neighborhood radius"
MinPts = Your "minimum group size"

Remember: HIGH density = HIGH neighbors count
LOW density = LOW neighbors count

text

---

*"DBSCAN finds clusters by looking for crowded neighborhoods, not by measuring distance from center."*