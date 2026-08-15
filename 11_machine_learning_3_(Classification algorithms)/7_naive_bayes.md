Naive Bayes --- Detailed Notes

1. What is Naive Bayes?

Naive Bayes is a supervised probabilistic machine-learning algorithm based on Bayes' Theorem. It is mainly used for classification,including binary and multiclass classification.

It combines:

Bayes' Theorem

A naive conditional-independence assumption between features given the target class.

The central idea is:

Given the output class y, Naive Bayes assumes that the features x₁, x₂, ..., xₙ are conditionally independent.

2. Probability Basics

Events

An event is an outcome or collection of outcomes that we are interested in.

For events A and B, we can ask:

P(A)
P(B)
P(A and B)
P(B | A)
P(A | B)

Independent Events

A and B are independent when knowing that one occurred does notchange the probability of the other:

$$P(B|A)=P(B)$$

and:

$$P(A|B)=P(A)$$

Therefore:

$$P(A \cap B)=P(A)P(B)$$

Example: the result of a coin toss and the result of a separate die rollare independent.

Dependent Events

Events are dependent when knowing one event changes the probability ofthe other:

$$P(B|A) \neq P(B)$$

Example: drawing two balls without replacement. The first draw changesthe composition of the bag, so the probability of the second drawdepends on the first.

3. Conditional Probability

Conditional probability means the probability of one event given that another event has occurred.

$$P(B|A)=\frac{P(A \cap B)}{P(A)}$$

Multiply by P(A):

$$P(A \cap B)=P(A)P(B|A)$$

This is the multiplication rule.

Similarly:

$$P(A|B)=\frac{P(A \cap B)}{P(B)}$$

Therefore:

$$P(A \cap B)=P(B)P(A|B)$$

Since:

$$P(A \cap B)=P(B \cap A)$$

we obtain:

$$\boxed{P(A)P(B|A)=P(B)P(A|B)}$$

4. Deriving Bayes' Theorem

Start with:

$$P(A)P(B|A)=P(B)P(A|B)$$

Divide both sides by P(B):

$$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$$

Therefore:

$$\boxed{P(A|B)=\frac{P(B|A)P(A)}{P(B)}}$$

This is Bayes' Theorem.

Four important terms

Term       Meaning

P(A|B)   PosteriorP(B|A)   LikelihoodP(A)     PriorP(B)     Evidence

So:

$$Posterior=\frac{Likelihood \times Prior}{Evidence}$$

5. Applying Bayes' Theorem to Machine Learning

Suppose the input has four features:

x₁, x₂, x₃, x₄

and the output/target is:

y

We want:

$$P(y|x_1,x_2,x_3,x_4)$$

Apply Bayes' Theorem:

\frac{P(y)P(x_1,x_2,x_3,x_4|y)}{P(x_1,x_2,x_3,x_4)}}$$

Interpretation:

P(y) = prior probability of the class.

P(x₁,x₂,x₃,x₄ | y) = probability of observing all features given the class.

P(x₁,x₂,x₃,x₄) = evidence.

P(y | x₁,x₂,x₃,x₄) = posterior probability of the class.

6. The Naive Assumption

The joint likelihood:

$$P(x_1,x_2,x_3,x_4|y)$$

can become difficult to calculate as the number of features increases.

Naive Bayes makes the simplifying assumption that the features areconditionally independent given y:

P(x_1|y)P(x_2|y)P(x_3|y)P(x_4|y)$$

For n features:

\prod_{i=1}^{n}P(x_i|y)}$$

This is why the algorithm is called Naive Bayes.

7. Very Important: What Is Independent?

A common misunderstanding is:

"Naive Bayes assumes x₁, x₂, x₃, ... are completely independent."

More precisely, it assumes:

$$\boxed{x_1,x_2,\ldots,x_n\text{ are conditionally independent GIVEN } y}$$

It does not necessarily assume:

$$P(x_1,x_2)=P(x_1)P(x_2)$$

in the real-world data distribution.

For example:

Age
Income
Education

may naturally be related.

Naive Bayes says that after conditioning on the class y, it will treat their contributions as independent for calculating the likelihood.

Conceptually:

             y
          /  |  \          x₁  x₂  x₃  x₄

The class y is the condition under which the feature-independence assumption is made.

8. Dependency of the Output Variable

The target y is not assumed to be independent of the features.

The model is specifically interested in:

$$P(y|x_1,x_2,\ldots,x_n)$$

The features provide evidence about the target class.

For example:

x₁ = Age
x₂ = Income
x₃ = Education
x₄ = Credit history

y = Loan approval

The goal is to estimate:

$$P(Loan\ Approval|Age,Income,Education,Credit\ History)$$

9. Naive Bayes Formula for N Features

Start with:

\frac{P(y)P(x_1,\ldots,x_n|y)}{P(x_1,\ldots,x_n)}$$

Using conditional independence:

\prod_{i=1}^{n}P(x_i|y)$$

Therefore:

\frac{P(y)\prod_{i=1}^{n}P(x_i|y)}{P(x_1,\ldots,x_n)}}$$

This is the central Naive Bayes equation.

10. Binary Classification

Suppose there are two classes:

y = Yes → 1
y = No  → 0

For a new input:

X = [x₁, x₂, x₃, x₄]

calculate:

$$P(Yes|X)$$

and:

$$P(No|X)$$

Then choose the class with the larger posterior probability:

$$\boxed{\hat y=\arg\max_y P(y|X)}$$

11. Probability of YES

Bayes' Theorem gives:

\frac{P(Yes)P(x_1,x_2,x_3,x_4|Yes)}{P(x_1,x_2,x_3,x_4)}$$

Using the Naive Bayes assumption:

P(x_1|Yes)P(x_2|Yes)P(x_3|Yes)P(x_4|Yes)$$

Therefore:

\frac{P(Yes)P(x_1|Yes)P(x_2|Yes)P(x_3|Yes)P(x_4|Yes)}{P(x_1,x_2,x_3,x_4)}}$$

For n features:

\frac{P(Yes)\prod_{i=1}^{n}P(x_i|Yes)}{P(x_1,\ldots,x_n)}}$$

12. Probability of NO

Similarly:

\frac{P(No)P(x_1,x_2,x_3,x_4|No)}{P(x_1,x_2,x_3,x_4)}$$

Using conditional independence:

P(x_1|No)P(x_2|No)P(x_3|No)P(x_4|No)$$

Therefore:

\frac{P(No)P(x_1|No)P(x_2|No)P(x_3|No)P(x_4|No)}{P(x_1,x_2,x_3,x_4)}}$$

For n features:

\frac{P(No)\prod_{i=1}^{n}P(x_i|No)}{P(x_1,\ldots,x_n)}}$$

13. Important Correction to the Formula

A common mistake is writing:

\frac{P(Yes)P(Yes|x_1)P(Yes|x_2)\cdots P(Yes|x_n)}{P(x_1)P(x_2)\cdots P(x_n)}$$

This is not the standard Naive Bayes formula.

The likelihood terms must be:

$$\boxed{P(x_i|Yes)}$$

not:

$$P(Yes|x_i)$$

So the correct numerator is:

$$\boxed{P(Yes)P(x_1|Yes)P(x_2|Yes)\cdotsP(x_n|Yes)}$$

Likewise for No:

$$\boxed{P(No)P(x_1|No)P(x_2|No)\cdotsP(x_n|No)}$$

14. Important Correction About the Denominator

The exact denominator is:

$$P(x_1,x_2,\ldots,x_n)$$

It is not automatically:

$$P(x_1)P(x_2)\cdots P(x_n)$$

That product would require an additional unconditional-independenceassumption about the features.

Naive Bayes normally assumes conditional independence:

\prod_iP(x_i|y)$$

not unconditional independence.

15. Why the Denominator Can Be Ignored for Classification

For the same input X:

\frac{P(Yes)P(X|Yes)}{P(X)}$$

and:

\frac{P(No)P(X|No)}{P(X)}$$

The denominator P(X) is the same for both classes.

Therefore, when only deciding which class is larger, we can compare:

$$Score(Yes)=P(Yes)P(X|Yes)$$

against:

$$Score(No)=P(No)P(X|No)$$

Using the Naive Bayes assumption:

P(Yes)\prod_{i=1}^{n}P(x_i|Yes)$$

and:

P(No)\prod_{i=1}^{n}P(x_i|No)$$

Then:

If Score(Yes) > Score(No):
    prediction = Yes

Otherwise:
    prediction = No

16. Numerical Binary Classification Example

Suppose:

P(Yes) = 0.60
P(No)  = 0.40

For a new observation with three features:

P(x₁|Yes) = 0.80
P(x₂|Yes) = 0.70
P(x₃|Yes) = 0.90

Then:

0.60(0.80)(0.70)(0.90)

0.3024$$

Suppose:

P(x₁|No) = 0.30
P(x₂|No) = 0.40
P(x₃|No) = 0.20

Then:

0.40(0.30)(0.40)(0.20)

0.0096$$

Since:

$$0.3024>0.0096$$

the prediction is:

Yes → 1

If normalized posterior probabilities are required:

\frac{0.3024}{0.3024+0.0096}\approx 0.9692$$

\frac{0.0096}{0.3024+0.0096}\approx 0.0308$$

So approximately:

P(Yes | X) = 96.92%
P(No  | X) = 3.08%

17. Why Naive Bayes Can Still Work

Real-world features are often not perfectly independent.

For example:

Age ↔ Income
Education ↔ Income

may be correlated.

Nevertheless, Naive Bayes can still perform well because classificationoften only needs to identify which class has the highest posteriorprobability.

Therefore:

The independence assumption can be unrealistic, but the classifier canstill be highly useful in practice.

18. Naive Bayes Variants

Gaussian Naive Bayes

For continuous numerical features, Gaussian Naive Bayes models eachfeature's distribution within a class using a Gaussian/normaldistribution.

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

Examples of numerical features:

Age
Salary
Height
Weight
Temperature

Multinomial Naive Bayes

Common for count-based features, especially text.

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

Typical uses:

Spam detection
Text classification
Document classification
Word-count features

Bernoulli Naive Bayes

Useful for binary features:

0 / 1
True / False
Present / Absent

from sklearn.naive_bayes import BernoulliNB

Categorical Naive Bayes

Useful when features are categorical.

from sklearn.naive_bayes import CategoricalNB

19. Naive Bayes vs Other Classifiers

Naive Bayes is useful when:

You want a fast baseline.

You have many features.

You are working with text.

You need fast training and prediction.

A probabilistic model is useful.

The selected distributional assumptions are reasonably suitable.

You should experiment and compare it with:

Naive Bayes
Logistic Regression
KNN
Decision Tree
Random Forest
SVM
Gradient Boosting

Compare using appropriate metrics such as:

Accuracy

Precision

Recall

F1-score

Confusion matrix

Cross-validation score

20. Complete Mental Model

                 New Input
             X = [x₁,x₂,...,xₙ]
                       |
          +------------+------------+
          |                         |
          v                         v
      Assume YES                Assume NO
          |                         |
          v                         v
 P(Yes) × P(x₁|Yes)       P(No) × P(x₁|No)
          ×                         ×
      P(x₂|Yes)                P(x₂|No)
          ×                         ×
          ...                       ...
          ×                         ×
      P(xₙ|Yes)                P(xₙ|No)
          |                         |
          v                         v
     YES score                 NO score
          |                         |
          +------------+------------+
                       |
                       v
                Compare scores
                       |
                       v
                 Larger score
                       |
                       v
                  Prediction

21. Core Equations to Memorize

Conditional probability

$$P(B|A)=\frac{P(A\cap B)}{P(A)}$$

Joint probability

$$P(A\cap B)=P(A)P(B|A)$$

and:

$$P(A\cap B)=P(B)P(A|B)$$

Therefore:

$$P(A)P(B|A)=P(B)P(A|B)$$

Bayes' Theorem

$$\boxed{P(A|B)=\frac{P(B|A)P(A)}{P(B)}}$$

Naive Bayes

\frac{P(y)\prod_{i=1}^{n}P(x_i|y)}{P(x_1,\ldots,x_n)}}$$

Classification decision

\arg\max_yP(y)\prod_{i=1}^{n}P(x_i|y)}$$

22. Final One-Line Definition

Naive Bayes is a supervised probabilistic classification algorithmthat applies Bayes Theorem while assuming that the features are conditionally independent given the target class.

23. Quick Revision

Bayes:
P(A|B) = P(B|A)P(A) / P(B)

Joint probability:
P(A and B) = P(A)P(B|A)
P(A and B) = P(B)P(A|B)

Naive assumption:
x₁, x₂, ..., xₙ are conditionally independent GIVEN y.

For binary classification:
y = Yes → 1
y = No  → 0

YES score:
P(Yes) × Π P(xᵢ|Yes)

NO score:
P(No) × Π P(xᵢ|No)

Choose the class with the larger score.