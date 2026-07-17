# Conditional Probability

## Definition

Conditional probability is the probability that an event occurs **given that another event has already occurred**.

The word **"given"** is the key indicator that conditional probability should be used.

Examples:

- Probability that a student studies Mathematics **given** they study Physics.
- Probability that the second card is an Ace **given** the first card was an Ace.
- Probability that a patient has a disease **given** they tested positive.

---

# Formula


::contentReference[oaicite:0]{index=0}

P(A|B)=\frac{P(A\cap B)}{P(B)}

Where:

- **P(A|B)** = Probability of A given B
- **P(A ∩ B)** = Probability that both A and B occur
- **P(B)** = Probability that B has occurred

---

# Meaning of "Given"

The word **given** means that event **B has already happened**.

Instead of considering the entire sample space, we only consider the outcomes where **B** occurs.

Think of it as "zooming in" on event B.

---

# Example 1

A class has:

- 80 students
- 50 study Mathematics
- 30 study Physics
- 20 study both Mathematics and Physics

Find:

Probability that a student studies Mathematics **given** they study Physics.

### Solution

Given:

P(M ∩ P) = 20

P(P) = 30

\[
P(M|P)=\frac{20}{30}
=\frac23
\]

Answer:

\[
\boxed{\frac23}
\]

---

# Example 2

A deck has 52 cards.

One card is drawn.

Find the probability that the card is a King **given** it is a Face Card.

Face cards:

- Jack
- Queen
- King

Total face cards = 12

Kings = 4

\[
P(King|Face)=\frac4{12}
=\frac13
\]

---

# Example 3

A bag contains:

- 5 Red
- 3 Blue

One ball is drawn and not replaced.

Find the probability that the second ball is Red **given** the first ball was Red.

After removing one red ball:

Remaining:

- 4 Red
- 3 Blue

Total = 7

\[
P(R_2|R_1)=\frac47
\]

---

# Relationship with Multiplication Rule

The multiplication rule for dependent events comes directly from conditional probability.

Formula:

\[
P(A\cap B)=P(A)\times P(B|A)
\]

This is used whenever events are dependent.

Example:

Drawing two cards without replacement.

---

# Independent Events

If A and B are independent,

\[
P(A|B)=P(A)
\]

Why?

Because event B does not change the probability of event A.

Example:

Rolling a die and tossing a coin.

The die result does not affect the coin result.

---

# Conditional Probability vs Independent Probability

| Conditional Probability | Independent Probability |
|--------------------------|-------------------------|
| Uses "given" | No "given" |
| Depends on another event | Events do not affect each other |
| Sample space changes | Sample space remains the same |

---

# Common Keywords

Conditional Probability questions usually contain:

- given
- knowing that
- assuming
- if
- after
- already occurred

---

# Real-World Applications

Conditional probability is used in:

- Medical diagnosis
- Machine Learning
- Artificial Intelligence
- Spam detection
- Credit risk analysis
- Fraud detection
- Weather forecasting
- Recommendation systems
- Bayesian inference

---

# Common Mistakes

❌ Using:

P(A|B)=P(A)/P(B)

Incorrect

✔ Correct:

P(A|B)=P(A∩B)/P(B)

---

❌ Forgetting that "given" changes the sample space.

Always restrict the sample space to event B.

---

# Quick Revision

Definition:

Probability of A occurring after B has already occurred.

Formula:

P(A|B)=P(A∩B)/P(B)

Keywords:

- Given
- Knowing
- Assuming
- After

If events are independent:

P(A|B)=P(A)

If events are dependent:

Use

P(A∩B)=P(A)×P(B|A)

---

# What's Next in Statistics?

After Conditional Probability, the usual learning path is:

1. Random Variables
2. Probability Distributions
3. Bernoulli Distribution
4. Binomial Distribution
5. Poisson Distribution
6. Continuous Probability Distributions
7. Normal Distribution
8. Expected Value
9. Variance
10. Standard Deviation
11. Sampling Distributions
12. Central Limit Theorem