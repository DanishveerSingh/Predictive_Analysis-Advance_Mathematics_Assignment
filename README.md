# Title: Probability Density Function using Non-Linear Model

# 1. Methodology
Data Collection ----> Column Selection ---> Data Transformation ----> Parameters and Probability function estimation ----> Parameters printing

# 2. Description
- Dataset: data.csv
- Target Column: no2
- Transformation of no2 column by the formula z = Tr(x) = x + asin(bx)
- Learning parameters by using the function p(z) = c * e ^ (-lamda * (z - mu) ^ 2)

# 3. Objectives
- Transformation of data
- Handle parameters estimation
- Apply estimation techniques
- Printing optimal values of parameters (lamda, mu, c)

# 4. Results
<img width="554" height="89" alt="image" src="https://github.com/user-attachments/assets/f8617d71-a5ba-486e-bfb4-cb19f1472e05" />
