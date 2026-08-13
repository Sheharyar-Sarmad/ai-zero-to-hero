Bayes' Theorem - Comprehensive Notes
1. Introduction
Bayes' Theorem is a fundamental concept in probability theory and statistics that describes the probability of an event based on prior knowledge of conditions that might be related to the event.

Historical Context
Named after Thomas Bayes (1701-1761)

Published posthumously in 1763

Later developed and popularized by Pierre-Simon Laplace

2. The Formula
Basic Form
P
(
A
∣
B
)
=
P
(
B
∣
A
)
⋅
P
(
A
)
P
(
B
)
P(A∣B)= 
P(B)
P(B∣A)⋅P(A)
​
 

Where:

P
(
A
∣
B
)
P(A∣B) = Posterior Probability: Probability of A given B

P
(
B
∣
A
)
P(B∣A) = Likelihood: Probability of B given A

P
(
A
)
P(A) = Prior Probability: Initial probability of A

P
(
B
)
P(B) = Evidence/Total Probability: Probability of B

Expanded Form (Law of Total Probability)
P
(
A
∣
B
)
=
P
(
B
∣
A
)
⋅
P
(
A
)
P
(
B
∣
A
)
P
(
A
)
+
P
(
B
∣
A
c
)
P
(
A
c
)
P(A∣B)= 
P(B∣A)P(A)+P(B∣A 
c
 )P(A 
c
 )
P(B∣A)⋅P(A)
​
 

3. Key Terminology
Term	Symbol	Description	Example
Prior	
P
(
A
)
P(A)	Initial belief before seeing evidence	Probability of having a disease before testing
Likelihood	
P
(
B
∥
A
)
P(B∥A)	Probability of evidence given hypothesis	Test accuracy (true positive rate)
Evidence	
P
(
B
)
P(B)	Total probability of evidence	Overall probability of positive test
Posterior	
P
(
A
∥
B
)
P(A∥B)	Updated belief after seeing evidence	Probability of disease after positive test
4. Example Problems
Example 1: Medical Testing
Problem: A disease affects 1% of the population. A test has:

95% true positive rate

90% true negative rate

Solution:

Given:

P
(
D
)
=
0.01
P(D)=0.01 (Prior)

P
(
+
∣
D
)
=
0.95
P(+∣D)=0.95 (Sensitivity)

P
(
−
∣
D
c
)
=
0.90
P(−∣D 
c
 )=0.90 (Specificity)

Therefore:

P
(
+
∣
D
c
)
=
1
−
0.90
=
0.10
P(+∣D 
c
 )=1−0.90=0.10 (False positive rate)

Calculate 
P
(
D
∣
+
)
P(D∣+):

P
(
D
∣
+
)
=
0.95
×
0.01
(
0.95
×
0.01
)
+
(
0.10
×
0.99
)
P(D∣+)= 
(0.95×0.01)+(0.10×0.99)
0.95×0.01
​
 

P
(
D
∣
+
)
=
0.0095
0.0095
+
0.099
=
0.0095
0.1085
≈
0.0876
P(D∣+)= 
0.0095+0.099
0.0095
​
 = 
0.1085
0.0095
​
 ≈0.0876

Interpretation: Only 8.76% probability of disease after positive test!

Example 2: Weather Forecast
Problem:

Probability of rain: 
P
(
R
)
=
0.30
P(R)=0.30

If raining, forecast says rain: 
P
(
F
∣
R
)
=
0.90
P(F∣R)=0.90

If not raining, forecast says rain: 
P
(
F
∣
R
c
)
=
0.20
P(F∣R 
c
 )=0.20

Find probability it actually rains given forecast says rain:

P
(
R
∣
F
)
=
0.90
×
0.30
(
0.90
×
0.30
)
+
(
0.20
×
0.70
)
P(R∣F)= 
(0.90×0.30)+(0.20×0.70)
0.90×0.30
​
 

P
(
R
∣
F
)
=
0.27
0.27
+
0.14
=
0.27
0.41
≈
0.6585
P(R∣F)= 
0.27+0.14
0.27
​
 = 
0.41
0.27
​
 ≈0.6585

Interpretation: 65.85% chance of rain when forecast predicts rain.

5. Applications
Real-World Applications:
Medical Diagnostics: Disease screening

Machine Learning: Naive Bayes classifiers

Spam Detection: Email filtering

Finance: Risk assessment

Law: Evidence evaluation

Artificial Intelligence: Bayesian networks

Python Implementation:
python
def bayes_theorem(prior, likelihood, evidence):
    """
    Calculate posterior probability using Bayes' Theorem
    """
    posterior = (likelihood * prior) / evidence
    return posterior

# Example usage
prior = 0.01  # Disease prevalence
likelihood = 0.95  # True positive rate
evidence = 0.1085  # Total probability of positive test
result = bayes_theorem(prior, likelihood, evidence)
print(f"Posterior probability: {result:.4f}")
6. Bayesian vs Frequentist
Aspect	Bayesian	Frequentist
Probability	Degree of belief	Long-run frequency
Parameters	Random variables	Fixed constants
Prior	Required	Not used
Interpretation	Subjective	Objective
Updating	Continuous	Hypothesis testing
7. Common Misconceptions
❌ Base Rate Fallacy: Ignoring prior probabilities

❌ Confusing P(A|B) with P(B|A): Prosecutor's fallacy

❌ Assuming independence when events are dependent

8. Advanced Concepts
Bayesian Updating
When new evidence arrives, the posterior becomes the new prior:

P
(
A
∣
new data
)
∝
P
(
new data
∣
A
)
⋅
P
(
A
∣
old data
)
P(A∣new data)∝P(new data∣A)⋅P(A∣old data)

Odds Form
P
(
A
∣
B
)
P
(
A
c
∣
B
)
=
P
(
B
∣
A
)
P
(
B
∣
A
c
)
⋅
P
(
A
)
P
(
A
c
)
P(A 
c
 ∣B)
P(A∣B)
​
 = 
P(B∣A 
c
 )
P(B∣A)
​
 ⋅ 
P(A 
c
 )
P(A)
​
 

Posterior Odds = Likelihood Ratio × Prior Odds

9. Practice Problems
Problem 1
A factory has 3 machines producing items:

Machine A: 50% production, 2% defective

Machine B: 30% production, 3% defective

Machine C: 20% production, 4% defective

If an item is defective, what's probability it came from Machine A?

Problem 2
A test for a disease has 99% sensitivity and 99% specificity.
If disease prevalence is 0.1%, what's P(D|positive test)?

Problem 3
Two coins: one fair, one double-headed.
Randomly pick a coin, flip it twice, both heads.
What's probability you picked the double-headed coin?

10. Key Takeaways
Bayes' Theorem updates beliefs based on new evidence

Prior matters: Base rates significantly impact results

Not intuitive: Our gut often ignores base rates

Widely applicable: From medicine to AI

Always consider: Evidence, Prior, and Likelihood

11. Additional Resources
Books: "Bayesian Data Analysis" by Gelman et al.

Online:

Khan Academy: Bayes Theorem

3Blue1Brown: Bayesian reasoning

Software: PyMC3, Stan, JAGS

12. Quick Reference Card
text
Bayes' Theorem: P(A|B) = P(B|A)P(A) / P(B)

When to use:
✓ Updating beliefs with evidence
✓ Inverse probability problems
✓ Classification tasks
✓ Diagnostic testing

Remember:
• P(A|B) ≠ P(B|A)
• Always consider prior probabilities
• Evidence must be total probability
Last Updated: 2026-07-14
Version: 1.0