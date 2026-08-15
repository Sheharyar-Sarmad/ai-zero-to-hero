# Convergence Theorems in Linear Regression

## Context
In linear regression, we typically solve:
\[
\min_{\beta \in \mathbb{R}^p} \| y - X\beta \|_2^2
\]
where:
- \( y \in \mathbb{R}^n \) = response vector
- \( X \in \mathbb{R}^{n \times p} \) = design matrix
- \( \beta \) = coefficient vector

Convergence appears in two main areas:
1. **Algorithmic convergence** (optimization methods)
2. **Statistical convergence** (asymptotic properties of estimators)

---

## 1. Algorithmic Convergence Theorems

### 1.1 Gradient Descent (GD) for OLS

**Loss function:** \( L(\beta) = \frac{1}{2n} \| y - X\beta \|^2 \)

**Gradient:** \( \nabla L(\beta) = -\frac{1}{n} X^T (y - X\beta) \)

**Update rule:**
\[
\beta_{k+1} = \beta_k - \eta \nabla L(\beta_k)
\]
where \( \eta > 0 \) is the learning rate.

#### Convergence Theorem (Strongly Convex Case):
If \( 0 < \eta < \frac{2}{\lambda_{\max}(X^T X)} \), then
\[
L(\beta_k) - L(\beta^*) \le \left(1 - \eta \lambda_{\min}(X^T X)\right)^k \left[ L(\beta_0) - L(\beta^*) \right]
\]
where \( \beta^* = (X^T X)^{-1} X^T y \) is the OLS solution.

**Key points:**
- **Linear convergence** rate (exponential decay)
- Convergence rate governed by condition number:
  \[
  \kappa = \frac{\lambda_{\max}}{\lambda_{\min}}
  \]
- Poorly conditioned \(X\) (large \(\kappa\)) → slow convergence

---

### 1.2 Stochastic Gradient Descent (SGD)

**Update rule (with mini-batch or single sample):**
\[
\beta_{k+1} = \beta_k - \eta_k \nabla L_i(\beta_k)
\]

#### Convergence Theorem (Robbins-Monro conditions):
If step sizes satisfy:
\[
\sum_{k=1}^\infty \eta_k = \infty \quad \text{and} \quad \sum_{k=1}^\infty \eta_k^2 < \infty
\]
then \(\beta_k \to \beta^*\) almost surely (for convex, smooth losses).

**Common choice:** \( \eta_k = \frac{c}{k} \) or \( \eta_k = \frac{c}{\sqrt{k}} \)

**Convergence rate:** \( \mathbb{E}[\|\beta_k - \beta^*\|^2] = O\left(\frac{1}{k}\right) \) (sublinear)

---

### 1.3 Newton's Method

**Update:**
\[
\beta_{k+1} = \beta_k - \left( \nabla^2 L(\beta_k) \right)^{-1} \nabla L(\beta_k)
\]
For OLS, this is exactly:
\[
\beta_{k+1} = \beta_k - (X^T X)^{-1} X^T (X\beta_k - y) = \beta^* \quad \text{in one step!}
\]
(Since OLS is quadratic, Newton converges in a single iteration.)

---

## 2. Statistical Convergence Theorems

### 2.1 Law of Large Numbers (LLN) for OLS

Under i.i.d. observations \((x_i, y_i)\):
\[
\frac{1}{n} X^T X \xrightarrow{p} \mathbb{E}[x_i x_i^T]
\]
\[
\frac{1}{n} X^T y \xrightarrow{p} \mathbb{E}[x_i y_i]
\]

**Consequence:** OLS estimator converges in probability:
\[
\hat{\beta}_n \xrightarrow{p} \beta^* = \mathbb{E}[x_i x_i^T]^{-1} \mathbb{E}[x_i y_i]
\]

---

### 2.2 Central Limit Theorem (CLT) for OLS

With i.i.d. errors \(\varepsilon_i\) (mean 0, variance \(\sigma^2\)):
\[
\sqrt{n} (\hat{\beta}_n - \beta^*) \xrightarrow{d} \mathcal{N}\left(0, \sigma^2 \, \mathbb{E}[x_i x_i^T]^{-1} \right)
\]

**Key conditions:**
- \( \mathbb{E}[\varepsilon_i | x_i] = 0 \) (exogeneity)
- \( \mathbb{E}[x_i x_i^T] \) is positive definite
- \( \mathbb{E}[\varepsilon_i^2 | x_i] = \sigma^2 \) (homoscedasticity)

---

### 2.3 Consistency Theorem

An estimator \(\hat{\beta}_n\) is **consistent** if:
\[
\hat{\beta}_n \xrightarrow{p} \beta^*
\]

**Sufficient conditions for OLS consistency:**
1. \( \frac{1}{n} X^T X \to Q \) (positive definite)
2. \( \frac{1}{n} X^T \varepsilon \xrightarrow{p} 0 \)

---

### 2.4 Convergence in Mean Square

\[
\mathbb{E}[\|\hat{\beta}_n - \beta^*\|^2] \to 0
\]
This implies consistency and is often shown via:
\[
\text{MSE} = \text{Bias}^2 + \text{Variance} \to 0
\]
For OLS:
- **Bias = 0** (unbiased if \( \mathbb{E}[\varepsilon|X] = 0 \))
- **Variance** \( = \sigma^2 (X^T X)^{-1} \to 0 \) (if eigenvalues grow)

---

## 3. Regularized Regression Convergence

### 3.1 Ridge Regression

**Objective:** \( \min_\beta \| y - X\beta \|^2 + \lambda \|\beta\|^2 \)

**Solution:** \( \hat{\beta}_{\text{ridge}} = (X^T X + \lambda I)^{-1} X^T y \)

**Convergence:** As \( n \to \infty \), under mild conditions:
\[
\hat{\beta}_{\text{ridge}} \xrightarrow{p} \beta^* \quad \text{(if } \lambda = o(n) \text{)}
\]
Bias-variance trade-off governs finite-sample convergence.

---

### 3.2 Lasso Regression

**Objective:** \( \min_\beta \| y - X\beta \|^2 + \lambda \|\beta\|_1 \)

**Convergence properties:**
- **Algorithmic:** Proximal gradient / coordinate descent converges linearly (for certain conditions).
- **Statistical:** Lasso is consistent if \( \lambda_n \to 0 \) and \( \lambda_n \sqrt{n} \to \infty \) (irrepresentable condition for sign consistency).

---

## 4. Convergence Diagnostics in Practice

| Method | Convergence Criterion |
|--------|------------------------|
| **Gradient Descent** | \( \|\nabla L(\beta_k)\| < \epsilon \) or \( |L(\beta_k) - L(\beta_{k-1})| < \epsilon \) |
| **OLS closed form** | Exact (one-step convergence) |
| **SGD** | Monitor validation loss, use early stopping |
| **MCMC (Bayesian linear regression)** | Trace plots, Gelman-Rubin statistic |

---

## Summary Table

| Type | Theorem | Rate |
|------|---------|------|
| **Algorithmic** (GD) | Linear convergence | \( O(\rho^k) \), \( \rho < 1 \) |
| **Algorithmic** (SGD) | Sublinear | \( O(1/\sqrt{k}) \) or \( O(1/k) \) |
| **Statistical** (LLN) | Consistency | \( \hat{\beta}_n \xrightarrow{p} \beta^* \) |
| **Statistical** (CLT) | Asymptotic normality | \( \sqrt{n}(\hat{\beta}_n - \beta^*) \xrightarrow{d} \mathcal{N}(0, \Sigma) \) |

---

## Important Caveats

- **Perfect multicollinearity** → no unique solution ( \(X^T X\) singular ), convergence fails
- **High-dimensional** (\(p > n\)) → OLS not identifiable; need regularization
- **Non-convex penalties** (e.g., SCAD, MCP) → convergence only to local minima
- **SGD convergence** depends heavily on learning rate scheduling