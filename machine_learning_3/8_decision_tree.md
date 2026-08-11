Decision Tree — Complete Notes

Core idea: A Decision Tree is a supervised learning algorithm that makes predictions by asking a sequence of questions.Conceptually, it behaves like a learned if / elif / else structure.

1. Decision Tree in the Simplest Way

A Decision Tree can be understood as:

if condition:
    decision_1
elif condition:
    decision_2
else:
    decision_3

The important difference is:

In normal programming, we manually write the conditions.

In Machine Learning, the Decision Tree learns useful conditions/splits from the training data.

For example, a model might learn rules such as:

Income <= 50000?
Credit Score <= 650?
Age <= 35?

and use them to reach a final prediction.

2. Money Example — Decision Tree as if / elif / else

Suppose:

money = ?

and our decisions are:

if money < 30:
    Snack

elif money < 60:
    Fast Food

elif money < 90:
    Dinner

else:
    5 Star

A simple tree representation is:

                         money < 30?
                        /           \
                     True           False
                      |               |
                    Snack          money < 60?
                                  /           \
                               True           False
                                |               |
                            Fast Food       money < 90?
                                          /           \
                                       True           False
                                        |               |
                                     Dinner           5 Star

Example 1

money = 20

The tree asks:

20 < 30 ?

Yes → go to the True branch → Snack.

Example 2

money = 45

First:

45 < 30 → False

So continue.

45 < 60 → True

Therefore:

Fast Food

Example 3

money = 75

75 < 30 → False
75 < 60 → False
75 < 90 → True

Therefore:

Dinner

Example 4

money = 100

100 < 30 → False
100 < 60 → False
100 < 90 → False

Therefore:

5 Star

Important

The cleaner Python version is:

if money < 30:
    snack
elif money < 60:
    fast_food
elif money < 90:
    dinner
else:
    five_star

We do not need to write money > 30 in the second condition because if the first condition failed, we already know:

money >= 30

3. The Basic Structure of a Decision Tree

A Decision Tree contains:

Root
  ↓
Branches
  ↓
Decision/Internal Nodes
  ↓
Branches
  ↓
Leaf Nodes

The easiest way to remember them:

Term

Simplest meaning

Root

First decision/question

Branch

Path/outcome from a decision

Node

A point in the tree

Internal/Decision Node

A node that performs another split

Leaf

Final/terminal node where prediction is made

4. Root Node

The root node is the first decision in the tree.

Example:

                Outlook
               /   |    \
           Sunny Overcast Rain

Here:

Outlook

is the root.

All training observations start at the root.

Easiest way to identify the root

Look at the top-most decision of the tree.

             ROOT
               ↓
            Outlook
          /    |    \
       Sunny Overcast Rain

Outlook is the root.

5. Branch

A branch is the path created by the outcome of a decision.

For example:

                 Outlook
              /     |      \
           Sunny  Overcast  Rain

There are branches corresponding to:

Sunny
Overcast
Rain

For a binary numerical decision:

              Age < 30?
              /       \
           True       False

the branches are:

True
False

Easy identification

If it is the line/path connecting one decision to another, think:

Branch

6. Node

A node is a point/location in the tree.

Example:

                    Outlook
                   /   |   \
               Sunny Overcast Rain
                 |
             Temperature

These are nodes:

Outlook
Sunny
Overcast
Rain
Temperature

More specifically, nodes can play different roles:

Root Node
Internal/Decision Node
Leaf Node

7. Internal / Decision Node

An internal node is a node that still makes another decision.

Example:

                 Sunny
                   |
              Temperature
               /   |   \
             Hot  Mild  Cool

Temperature is an internal/decision node because it splits the data again.

It is not yet the final prediction.

8. Leaf Node

A leaf node is a terminal node.

The tree stops there and produces the prediction.

Example:

              Temperature
               /       \
             Hot       Cool
              |          |
             No         Yes
             ↑           ↑
           LEAF        LEAF

No and Yes are the final predictions.

Easiest way to identify a leaf

Ask:

"Can the tree continue from this point?"

If there is no further split:

             Yes
              ↑
            LEAF

it is a leaf.

9. Root vs Branch vs Leaf — Fast Identification

Use this rule:

TOP       → Root
LINES     → Branches
MIDDLE    → Decision/Internal Nodes
END       → Leaves

Example:

                    Outlook       ← ROOT
                   /   |   \
                  /    |    \
              Sunny Overcast Rain ← branches lead here
                |
           Temperature              ← INTERNAL NODE
             /   |   \
            /    |    \
          Hot   Mild  Cool
           |     |     |
          No    Yes    Yes          ← LEAVES

10. Play Tennis / "Playing Guess" Example

The first screenshot uses the classic Play Tennis dataset.

The target/output variable is:

Play

with two classes:

Yes
No

Features include:

Outlook
Temperature
Humidity
Wind

The dataset has 14 observations.

The target counts are:

Yes = 9
No  = 5

So the tree begins with all 14 observations.

11. Why Is Outlook the Root?

This is one of the most important questions in Decision Trees.

The algorithm does not randomly choose the root.

It evaluates possible features and asks:

"Which feature produces the best separation of the target classes?"

Common criteria include:

Entropy
Information Gain
Gini Impurity

The screenshots are using:

Entropy + Information Gain

For this dataset, Outlook has the highest Information Gain among the features shown.

Therefore:

Root = Outlook

12. First Split Using Outlook

The root is:

                    Outlook
                 /     |      \
              Sunny  Overcast  Rain

The dataset is divided into three groups.

Sunny

There are 5 Sunny observations:

Yes = 2
No  = 3

So:

Sunny → 2 Yes / 3 No

This node is mixed/impure.

Overcast

There are 4 Overcast observations:

Yes = 4
No  = 0

So:

Overcast → 4 Yes / 0 No

This is a pure node.

Therefore it can become:

Overcast
    |
   Yes

Rain

There are 5 Rain observations:

Yes = 3
No  = 2

So:

Rain → 3 Yes / 2 No

This is also mixed/impure.

13. Why Do Sunny and Rain Continue?

Look at the results:

Sunny:
2 Yes
3 No

Mixed.

Overcast:
4 Yes
0 No

Pure.

Rain:
3 Yes
2 No

Mixed.

Therefore the tree can stop at:

Overcast → Yes

but needs more splitting for:

Sunny
Rain

Conceptually:

                       Outlook
                  /       |       \
               Sunny   Overcast    Rain
                |         |         |
              mixed      pure      mixed
                |         |         |
             split       leaf     split

14. Sunny Branch

For the Sunny observations:

Sunny → 2 Yes / 3 No

The algorithm can evaluate remaining features such as:

Temperature
Humidity
Wind

and choose the best available split for that subset.

In the screenshot, the next split is represented using:

Temperature

giving:

                    Sunny
                  /   |    \
                Hot  Mild  Cool

For example, Sunny + Hot gives:

No
No

so:

Sunny → Hot → No

is pure and can become a leaf.

The remaining Sunny subsets can be considered for further splitting if necessary.

15. Rain Branch

Rain contains:

3 Yes
2 No

so it is mixed.

The algorithm again evaluates remaining features to find a useful split.

A common resulting structure for this classic dataset is:

                  Rain
                 /    \
              Weak    Strong
                |        |
               Yes       No

Because:

Rain + Weak:
Yes
Yes
Yes

is pure.

And:

Rain + Strong:
No
No

is pure.

So the resulting nodes can become leaves.

16. Purity

Purity describes how homogeneous the target classes are inside a node.

Suppose a node contains:

Yes
Yes
Yes
Yes

Then:

100% Yes
0% No

This is perfectly pure.

Another node:

Yes
Yes
No
No

contains:

50% Yes
50% No

This is highly mixed/impure.

17. Pure Node

A node is pure when all observations inside it belong to one target class.

Examples:

Yes
Yes
Yes

or:

No
No
No

For a binary classification problem:

P(Yes) = 1
P(No)  = 0

or:

P(Yes) = 0
P(No)  = 1

18. Impure Node

A node is impure when it contains multiple target classes.

Example:

Yes
Yes
No
Yes
No

Counts:

Yes = 3
No  = 2

Therefore:

P(Yes) = 3/5 = 0.6
P(No)  = 2/5 = 0.4

The node is mixed.

The tree tries to find another split that makes the resulting child nodes more homogeneous.

19. Purity and Leaf Are NOT the Same Thing

This distinction is extremely important.

Purity

Purity describes the composition of the data.

Pure:
Yes Yes Yes Yes

Leaf

Leaf describes the position/role in the tree.

No further split
      ↓
    LEAF

Therefore:

Purity = property of the data in a node
Leaf   = terminal position in the tree

A pure node will often become a leaf.

But they are not synonyms.

20. Can a Leaf Be Impure?

Yes.

A Decision Tree may stop because of a stopping condition such as:

max_depth=3

or:

min_samples_leaf=5

Then a leaf might contain:

Yes
Yes
No

It is:

Impure

but still:

Leaf

because the algorithm has stopped splitting.

The prediction is usually based on the majority class.

Here:

Yes = 2
No  = 1

so prediction:

Yes

21. Why Does the Tree Want Purity?

Imagine:

Parent:

Yes Yes Yes No No No

This is mixed.

Now suppose a split produces:

Left:
Yes Yes Yes

Right:
No No No

Now both children are pure.

This is a very useful split.

The general idea is:

Mixed parent
     ↓
Good split
     ↓
More homogeneous children
     ↓
Pure / purer nodes
     ↓
Leaves

Entropy and Information Gain help the algorithm measure this.

22. Entropy

Entropy measures impurity/uncertainty in a node.

For a binary classification problem:

             n
            ---
            ↓
       - Σ pᵢ log₂(pᵢ)

More explicitly:

Entropy(S)
=
-p(Yes) log₂(p(Yes))
-p(No)  log₂(p(No))

For n classes:

Entropy(S) = - Σ pᵢ log₂(pᵢ)

where:

pᵢ = probability/proportion of class i in the node

23. Why Is There a Negative Sign?

Because for probabilities between 0 and 1:

log₂(p)

is negative.

For example:

log₂(0.5) = -1

So:

-p log₂(p)

turns the contribution into a positive number.

Therefore entropy is non-negative.

24. Entropy of the Entire Play Dataset

The dataset has:

Yes = 9
No  = 5
Total = 14

Therefore:

P(Yes) = 9/14
P(No)  = 5/14

The entropy is:

Entropy(Play)
=
-(9/14) log₂(9/14)
-(5/14) log₂(5/14)

Approximately:

Entropy(Play) ≈ 0.940

This is the 0.94 shown in the screenshot.

25. Understanding the Entropy Value

For binary classification:

Pure node:

Yes Yes Yes Yes

Entropy = 0

Because:

P(Yes) = 1
P(No) = 0

There is no uncertainty.

For a 50/50 binary node:

Yes Yes
No  No

Entropy is:

1

This is maximum uncertainty for a binary classification problem.

So, for binary classification:

Entropy = 0
     ↓
Pure / no uncertainty

Entropy = 1
     ↓
Maximum uncertainty at 50/50

26. Entropy of Sunny

Sunny contains:

Yes = 2
No  = 3
Total = 5

Therefore:

P(Yes) = 2/5
P(No)  = 3/5

Formula:

Entropy(Sunny)
=
-(2/5) log₂(2/5)
-(3/5) log₂(3/5)

Approximately:

Entropy(Sunny) ≈ 0.971

This is the 0.971 shown in the screenshot.

27. Entropy of Overcast

Overcast contains:

Yes = 4
No  = 0

Therefore:

P(Yes) = 1
P(No)  = 0

So:

Entropy(Overcast)
=
-(1)log₂(1)
-(0)log₂(0)

The result is:

Entropy(Overcast) = 0

This makes sense because the node is completely pure.

28. Entropy of Rain

Rain contains:

Yes = 3
No  = 2

Therefore:

P(Yes) = 3/5
P(No)  = 2/5

Formula:

Entropy(Rain)
=
-(3/5)log₂(3/5)
-(2/5)log₂(2/5)

Approximately:

Entropy(Rain) ≈ 0.971

Again, it is mixed, so entropy is greater than zero.

29. What the Screenshot Is Calculating

The screenshot calculates:

Play:

9 Yes
5 No

Entropy(Play) ≈ 0.94

Then it calculates entropy for the values of Outlook:

Sunny:
2 Yes / 3 No
Entropy ≈ 0.971

Overcast:
4 Yes / 0 No
Entropy = 0

Rain:
3 Yes / 2 No
Entropy ≈ 0.971

These child entropies are then used to calculate Information Gain.

30. Information Gain

Information Gain asks:

How much uncertainty did this split remove?

The basic formula is:

Information Gain
=
Parent Entropy
-
Weighted Average of Child Entropies

For feature Outlook:

IG(Play, Outlook)
=
Entropy(Play)
-
[
(5/14) Entropy(Sunny)
+
(4/14) Entropy(Overcast)
+
(5/14) Entropy(Rain)
]

Substitute the values:

IG(Play, Outlook)
=
0.940
-
[
(5/14)(0.971)
+
(4/14)(0)
+
(5/14)(0.971)
]

Approximately:

IG(Play, Outlook) ≈ 0.247

31. Why Are We Multiplying by 5/14, 4/14, 5/14?

Because the child groups have different sizes.

The original dataset contains:

14 observations

After splitting by Outlook:

Sunny     = 5
Overcast  = 4
Rain      = 5

Therefore:

Sunny weight    = 5/14
Overcast weight = 4/14
Rain weight     = 5/14

We calculate a weighted average because a child containing 5 observations should have more influence than a child containing 1 observation.

32. How Do We Decide the Root?

This is the complete process.

Suppose we have:

Features:

Outlook
Temperature
Humidity
Wind

We calculate Information Gain for each:

IG(Outlook)
IG(Temperature)
IG(Humidity)
IG(Wind)

For the classic Play Tennis data, approximately:

Outlook       → 0.247
Humidity      → 0.152
Wind          → 0.048
Temperature   → 0.029

Therefore:

Highest Information Gain = Outlook

So:

ROOT = Outlook

This is the key rule:

When using Information Gain, the feature with the highest Information Gain is selected as the split.

33. Why Does Highest Information Gain Win?

Because Information Gain tells us how much uncertainty is reduced.

Imagine:

Parent entropy = 0.94

Feature A reduces it to:

0.20

Feature B reduces it to:

0.70

Feature A removed more uncertainty.

Therefore:

Feature A → better split

and if it is the first split:

Feature A → root

34. Decision Tree Training Steps — Screenshot 3

The third screenshot shows the overall algorithm.

It can be understood as:

Step 1 — Start with the Data

Dataset
   ↓
Features + Target

Example:

Outlook
Temperature
Humidity
Wind
      ↓
    Play

All observations initially belong to one node.

Step 2 — Choose the Best Feature

Evaluate possible features using a splitting criterion.

For Information Gain:

Calculate:

IG(Outlook)
IG(Temperature)
IG(Humidity)
IG(Wind)

Choose the feature with the highest Information Gain.

In this example:

Outlook

wins.

So:

Root = Outlook

Step 3 — Make Branches

Split the dataset according to the selected feature.

                    Outlook
                 /     |      \
              Sunny  Overcast  Rain

Each outcome becomes a branch/subset.

Step 4 — Repeat the Process for Each Branch

This is the most important part.

For each subset:

Sunny
Overcast
Rain

ask:

Is the node pure enough / should we stop?

If not:

Choose another best feature
        ↓
Make another split
        ↓
Repeat

For example:

Sunny
  ↓
choose another feature
  ↓
Temperature
  ↓
Hot / Mild / Cool

35. Step 5 — When Does the Tree Stop?

The screenshot gives stopping conditions such as:

Condition 1 — All data is pure

Example:

Yes
Yes
Yes
Yes

No reason to split further.

Make a leaf:

Yes

Condition 2 — Maximum depth is reached

For example:

DecisionTreeClassifier(max_depth=3)

The tree stops growing after the allowed depth.

Other practical stopping/pruning conditions include:

min_samples_split
min_samples_leaf
max_leaf_nodes

These help prevent the tree from becoming unnecessarily complex.

36. Complete Decision Tree Learning Process

                 DATASET
                    |
                    ↓
          Calculate possible splits
                    |
                    ↓
            Choose best feature
                    |
                    ↓
                ROOT NODE
                    |
          +---------+---------+
          |         |         |
          ↓         ↓         ↓
       Branch    Branch    Branch
          |         |         |
          ↓         ↓         ↓
      Check purity / stopping condition
          |
       +--+--+
       |     |
      Stop  Continue
       |     |
      Leaf  Find best next split
             |
             ↓
          Repeat

37. The Relationship Between Entropy and Information Gain

Do not confuse these two.

Entropy

Measures:

How impure/uncertain is this node?

Entropy = uncertainty / impurity

Information Gain

Measures:

How much uncertainty did a split remove?

Information Gain
=
Parent Entropy
-
Weighted Child Entropy

Therefore:

Entropy
   ↓
Measure impurity

Information Gain
   ↓
Measure usefulness of a split

38. Simple Real-Life Analogy

Imagine you have 10 students:

6 like Python
4 like JavaScript

You want to separate them.

Current node:

Python = 6
JavaScript = 4

There is uncertainty.

Now suppose you split them by:

"Do they study Data Science?"

and get:

Data Science = Yes:
Python Python Python Python Python Python

Data Science = No:
JavaScript JavaScript JavaScript JavaScript

Excellent split.

The children are pure.

So:

High Information Gain

39. Decision Tree Does NOT Require Feature Scaling

An important practical point:

Decision Trees generally do not require standard scaling.

For example, you generally don't need:

from sklearn.preprocessing import StandardScaler

just to train a Decision Tree.

Why?

Because the tree makes decisions using conditions/splits such as:

Age <= 30
Income <= 50000

The relative ordering is what matters, rather than Euclidean distance or feature magnitude.

So unlike algorithms such as KNN, scaling is generally unnecessary for Decision Trees.

40. Classification Example

Suppose:

Age
Income
Credit Score

Target:

Loan Approved

A learned tree might look like:

                    Credit Score < 650?
                       /            \
                     Yes             No
                     /                \
              Income < 50K?         APPROVED
                /      \
              Yes      No
               |        |
            REJECT    APPROVED

Interpret it as:

if credit_score < 650:
    if income < 50000:
        Reject
    else:
        Approve
else:
    Approve

This is exactly why the if/else mental model is useful.

41. Prediction With a Decision Tree

Suppose a new observation is:

Credit Score = 620
Income = 70000

Start at root:

Credit Score < 650?

620 < 650 → True

Follow the True branch:

Income < 50000?

70000 < 50000 → False

Follow False:

APPROVED

The prediction is:

Approved

42. One Complete Mental Model

Think of the tree as a game of questions:

                   QUESTION 1
                       |
                +------+------+
                |             |
              YES            NO
                |             |
            QUESTION 2    QUESTION 3
             /    \         /    \
            /      \       /      \
         LEAF     LEAF   LEAF     LEAF

Every prediction travels:

Root
 ↓
Question
 ↓
Branch
 ↓
Question
 ↓
Branch
 ↓
Leaf
 ↓
Prediction

43. The Most Important Definitions to Memorize

Decision Tree

A supervised learning algorithm that makes predictions using a sequence of learned decision rules.

Root Node

The first/top-most decision node of the tree.

Branch

A path representing an outcome of a decision.

Internal/Decision Node

A node that performs another split.

Leaf Node

A terminal node where the tree stops splitting and produces a prediction.

Purity

How homogeneous the target classes are within a node.

Entropy

A measure of uncertainty/impurity in a node.

Information Gain

The reduction in entropy produced by a split.

44. Final Cheat Sheet

DECISION TREE
│
├── Root
│     └── First/best split
│
├── Branch
│     └── Path/outcome of a split
│
├── Internal Node
│     └── Another decision
│
└── Leaf
      └── Final prediction

Learning:

Dataset
   ↓
Calculate impurity
   ↓
Try possible features/splits
   ↓
Calculate Information Gain
   ↓
Highest IG → best split
   ↓
Create root
   ↓
Create branches
   ↓
Repeat for each non-terminal branch
   ↓
Stop when stopping condition is reached
   ↓
Leaf → prediction

Entropy:

Entropy(S)
=
-Σ pᵢ log₂(pᵢ)

Binary:

Entropy(S)
=
-P(Yes)log₂(P(Yes))
-P(No)log₂(P(No))

Information Gain:

IG(S, Feature)
=
Entropy(S)
-
Σ [ |Sᵥ| / |S| × Entropy(Sᵥ) ]

For Outlook:

Parent:

9 Yes
5 No

Entropy ≈ 0.940

Children:

Sunny:
2 Yes / 3 No
Entropy ≈ 0.971

Overcast:
4 Yes / 0 No
Entropy = 0

Rain:
3 Yes / 2 No
Entropy ≈ 0.971

Then:

IG(Outlook)
=
0.940
-
[
(5/14)(0.971)
+
(4/14)(0)
+
(5/14)(0.971)
]

≈ 0.247

Compare all candidate features:

Outlook      ≈ 0.247  ← highest
Humidity     ≈ 0.152
Wind         ≈ 0.048
Temperature  ≈ 0.029

Therefore:

ROOT = Outlook

45. One-Line Memory Trick

Remember:

Entropy tells us how confused the node is; Information Gain tells us which question reduces that confusion the most; the best question becomes the root or next decision node; branches represent its answers; and leaves give the final prediction.

