# T-Test: Complete Guide for Statistics & ML

## 📌 What is a T-Test?

A **t-test** is a statistical hypothesis test used to determine if there is a **significant difference** between the means of two groups. It's used when:
- Sample size is **small** (n < 30)
- Population standard deviation is **unknown**
- Data is approximately **normally distributed**

---

## 🎯 When to Use T-Test (Real-World)

| Scenario | Example |
|----------|---------|
| **A/B Testing** | Does new website design increase conversion rate? |
| **Medical Research** | Does Drug A lower blood pressure more than Drug B? |
| **Education** | Do students score higher after a new teaching method? |
| **ML Feature Analysis** | Is feature X significantly different between Class A and Class B? |
| **Quality Control** | Are products from Machine 1 vs Machine 2 same weight? |

---

## 📊 Types of T-Tests

| Type | Use Case | Formula |
|------|----------|---------|
| **One-Sample T-Test** | Compare sample mean to known population mean | $t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$ |
| **Independent Two-Sample T-Test** | Compare means of two independent groups | $t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$ |
| **Paired T-Test** | Compare means of same group at two times | $t = \frac{\bar{d}}{s_d / \sqrt{n}}$ |

## Formula

Z = (X̄₁ - X̄₂) / √(σ₁²/n₁ + σ₂²/n₂)

He's showing you two different formulas for comparing the means of two independent groups:

## Formula	Test	When to Use

Top (Z)	Two-Sample Z-Test	When you know the population standard deviations (σ₁ and σ₂)
Middle (t)	Two-Sample T-Test	When you DON'T know the population standard deviations (use sample std: s₁ and s₂)
Bottom	Degrees of Freedom	Approximate df for the t-test (conservative approach)
🔍 Breaking Down Each Part

## 1. Two-Sample Z-Test Formula

text
Z = (X̄₁ - X̄₂) / √(σ₁²/n₁ + σ₂²/n₂)
Symbol	Meaning
X̄₁	Mean of Group 1
X̄₂	Mean of Group 2
σ₁²	Population variance of Group 1 (KNOWN)
σ₂²	Population variance of Group 2 (KNOWN)
n₁	Sample size of Group 1
n₂	Sample size of Group 2
Use this when: You know the TRUE population standard deviation (rare in real life)

## 2. Two-Sample T-Test Formula

text
t = (X̄₁ - X̄₂) / √(s₁²/n₁ + s₂²/n₂)
Symbol	Meaning
X̄₁	Mean of Group 1
X̄₂	Mean of Group 2
s₁²	Sample variance of Group 1 (ESTIMATED from data)
s₂²	Sample variance of Group 2 (ESTIMATED from data)
n₁	Sample size of Group 1
n₂	Sample size of Group 2
Use this when: You DON'T know the population standard deviation (99% of real cases)

## 3. Degrees of Freedom (df)
text
df = min(n₁-1, n₂-1)
Symbol	Meaning
n₁-1	Degrees of freedom for Group 1
n₂-1	Degrees of freedom for Group 2
min()	Take the smaller of the two
Why? This is the conservative approach (Welch-Satterthwaite approximation simplified). Using the smaller df gives a more cautious test.

📝 Key Difference: Z vs T
Aspect	Z-Test	T-Test
Population std (σ)	✅ KNOWN	❌ UNKNOWN
Use sample std (s)	❌ NO	✅ YES
Sample size	Large (n ≥ 30)	Any size (even small)
When to use	Rare in real life	Almost always in ML/stats