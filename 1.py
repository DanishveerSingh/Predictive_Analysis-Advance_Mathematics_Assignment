# Importing Libraries
import pandas as pd
import numpy as np
import math
from scipy.optimize import minimize

# Loading Dataset
df = pd.read_csv("C:/Users/Acer/Downloads/data.csv", encoding = "latin1")
roll_number = 102317081

# Transforming Data
x = df["no2"].dropna().values.astype(float)
ar = 0.05 * (roll_number % 7)
br = 0.3 * ((roll_number % 5) + 1)
z = x + ar * np.sin(br * x)

# Parameters Estimation
def negative_log_likelihood(params, data):
    lam, mu, c = params
    if(lam <= 0 or c <= 0):
        return np.inf
    pdf = c * np.exp(-lam * (data - mu) ** 2)
    pdf = np.clip(pdf, 1e-12, None)
    return -np.sum(np.log(pdf))

initial_lam = 1.0 / (2 * np.var(z))
initial_mu = np.mean(z)
initial_c = 1.0
initial_params = [initial_lam, initial_mu, initial_c]
result = minimize(negative_log_likelihood, initial_params, args = (z,), method = "L-BFGS-B")
lamda, mu, c = result.x

# Output Parameters
print("Lamda:", lamda)
print("Mu:", mu)
print("C:", c)