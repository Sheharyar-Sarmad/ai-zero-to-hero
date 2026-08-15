


# What is Regression?
Supervised learning predicting continuous numerical output

Maps input features → real-valued number

Key distinction: Classification = categories, Regression = quantities

# Common Examples

Domain	Features	Target
Real Estate	Sq ft, bedrooms	House price ($)
Finance	Stock history	Stock price
Weather	Temp, humidity	Temperature

# Types 

Type	Description	When to Use
Simple Linear	y = mx + b	One input feature
Multiple Linear	y = b₀ + Σbᵢxᵢ	Multiple features, linear relationship
Polynomial	Features raised to powers	Non-linear relationships
Ridge (L2)	Penalizes large coefficients	Multicollinearity
Lasso (L1)	Can zero out coefficients	Feature selection
Tree-based	Random Forest, XGBoost	Complex interactions
Neural Network	Deep learning	Large datasets, complex patterns
Evaluation Metrics
Metric	Formula	Use
MSE	(1/n)Σ(y - ŷ)²	Penalizes large errors
RMSE	√MSE	Same units as target
MAE	(1/n)Σ|y - ŷ|	Robust to outliers
R²	1 - (SSres/SStot)	% variance explained (0-1)
Key Assumptions (Linear Regression)
Linearity - Linear relationship

Independence - Observations independent

Homoscedasticity - Constant residual variance

Normality - Residuals normally distributed

# Quick Code

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
python
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, preds)
r2 = r2_score(y_test, preds)
When to Use
✅ Use:

Output is continuous (price, age, temp)

Need numerical prediction

❌ Don't use:

Output is categorical → use classification

# Pros	Cons
Simple to interpret	Assumes linearity
Fast to train	Sensitive to outliers
Works well with small data	Can underfit complex patterns
Feature importance available	Requires feature scaling
Key Takeaway
Regression = Predicting how much (continuous)
Classification = Predicting which category (discrete)