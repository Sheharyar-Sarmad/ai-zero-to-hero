

<!-- Data Distribution --> 

A data distribution shows how data values are spread, and a Kernel Density Estimation (KDE) curve provides a smooth estimate of that distribution.

<!-- Example -->

Data:
2, 3, 3, 4, 5, 5, 5, 6, 7

KDE Curve

Density
 ^
 |             /\
 |            /  \
 |           /    \
 |__________/      \________
 +----------------------------> Values
   2  3  4  5  6  7

<!-- INTRODUCTION -->

In this section we will see how data distribution starts with a Histogram then it becomes a frequency polygon and eventually turns into a density curve that represents the distribution.

Histogram
↓
Frequency polygon
↓
Density curve

<!-- Normal Distribution(Bell shaped distribution) -->

A normal distribution is a symmetric, bell-shaped probability distribution where the mean, median, and mode are equal, and most observations are clustered around the center.

<!-- Example -->

Frequency

                 /\
               /    \
             /        \
           /            \
_________/              \_________

-------------------------------→ Values

<!-- Important Point -->

Before understanding Mean, Variance and Standard Deviation, we first have to understand the sample and population in statistics. 

<!-- Population -->

A population is the complete set of all individuals, objects, or observations that you want to study. It includes every member of the group.

<!-- Example  -->

Suppose a university has 20,000 students.

If you want to study all 20,000 students, then:
Population = 20,000 students

<!-- Sample -->

A sample is a smaller subset of the population that is selected to represent the entire population. Instead of studying everyone, you study only a few.

<!-- Example  -->

From the university of 20,000 students, you randomly select 500 students.

Population = 20,000 students
Sample = 500 students

You use the sample to estimate information about the whole population.

<!-- Variance -->

Variance is a statistical measure that quantifies the spread or dispersion of a set of data points around their mean (average). Variance is a measure of how far the data values are spread from the mean (average).

<!-- Simple Explanation -->

Variance tells us how far the data is spread from the mean.

Small variance → Data values are close to the mean.
Large variance → Data values are far from the mean.

<!-- Formula example -->

For finding variance we should have the mean as well without mean we cant find variance.

(data set 1st elem - mean) square + (data set 2nd elem - mean) square -- go untill n......

then evaluate all and the expression you get anwer and it will use in  the second step, in which we have to divide the answer by total number of data set elements

evaluated answer / total number data set elements = "variance"

(85−95)2 power + (90−95)2 power + (95−95) 2 power + (100−95) 2 power + (105−95) 2 = 250 
250 / 5 = 50 --variance

<!-- This is classic statistical formula of variance -->
σ² = (1/N) Σᵢ₌₁ᴺ (xᵢ − μ)²

σ² (Sigma Square) = Population Variance.

1/N = Divide by the total number of observations in the population.

N = Total number of observations in the population and if lower case(n) than its called the total observations in the sample.

Σ (Capital Sigma) = Summation (add all values together).

i = 1 = Start from the first observation.

N (above Σ) = Continue until the last (N-th) observation.

xᵢ = The i-th observation (current data value).

μ (Mu / Myoo) = Population Mean.

(xᵢ − μ) = Difference between the current observation and the population mean.

(xᵢ − μ)² = Square of the difference.

Finally, add all squared differences and divide by N to get the population variance.

<!-- Standard Deviation -->

Standard Deviation is a measure of spread that tells us how far data values are from the mean on average .Standard deviation measures the average distance of data values from the mean.

<!-- Formula -->

σ = √[(1/N) × Σ(i=1 to N) (xᵢ − μ)²]

<!-- Example -->

Suppose the data represents heights in centimeters.

After calculating variance, you get:

Variance = 64 cm²
Notice the unit: cm²

That's not easy to interpret because we usually measure height in cm, not cm².
So we take the square root of the variance.

Now: √64 = 8 cm