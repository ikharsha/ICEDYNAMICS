import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

from sklearn.linear_model import Lasso

from sklearn.linear_model import BayesianRidge
print("Linear Regrerssion")
#Output column change as per requirement



# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Train_data.csv')

# Get the column names from the DataFrame
column_names = df.columns.tolist()

# Assuming the last column is the target variable, and the rest are input variables
X = df[column_names[:-1]]  # Input variables
for i in range(5,8):
  y = df[column_names[i]]
  h=df.columns.values
  print("equation for ",h[i])
   # Target variable


  model = LinearRegression()
  model.fit(X, y)

    # Get the coefficients and intercept
  coefficients = model.coef_
  intercept = model.intercept_


  equation = "Target = "
  for i, col in enumerate(column_names[:-1]):
      equation += f"({coefficients[i]} * {col}) + "
  equation += str(intercept)

  print("Algebraic Equation:", equation)

#------------------------------------------------------------------------

print("SVR ALGORITHM")

#Output column change as per requirement


df = pd.read_csv('Train_data.csv')

# Get the column names from the DataFrame
column_names = df.columns.tolist()

# Assuming the last column is the target variable, and the rest are input variables
X = df[column_names[:-1]]  # Input variables
for i in range(5,8):
  y = df[column_names[i]]
  h=df.columns.values
  print("equation for ",h[i])# Target variable

    # Create and fit the SVR model with a linear kernel
  model = SVR(kernel='linear')
  model.fit(X, y)

    # Get the coefficients
  coefficients = model.coef_[0]
  intercept = model.intercept_[0]

    # Build the algebraic equation
  equation = "Target = "
  for i, col in enumerate(column_names[:-1]):
      equation += f"({coefficients[i]} * {col}) + "
  equation += str(intercept)

  print("Algebraic Equation:", equation)

#------------------------------------------------------------------------

print("bayesian ridge regression:-")
#Output column change as per requirement


df = pd.read_csv('Train_data.csv')

# Get the column names from the DataFrame
column_names = df.columns.tolist()

# Assuming the last column is the target variable, and the rest are input variables
X = df[column_names[:-1]]  # Input variables
for i in range(5,8):
  y = df[column_names[i]]
  h=df.columns.values
  print("equation for ",h[i])  # Target variable

    # Create and fit the Bayesian Ridge Regression model
  model = BayesianRidge()
  model.fit(X, y)

    # Get the coefficients
  coefficients = model.coef_
  intercept = model.intercept_

    # Build the algebraic equation
  equation = "Target = "
  for i, col in enumerate(column_names[:-1]):
      equation += f"({coefficients[i]} * {col}) + "
  equation += str(intercept)

  print("Algebraic Equation:", equation)

#-------------------------------------------------------

print("LASSO regression:-")



df = pd.read_csv('Train_data.csv')

# Get the column names from the DataFrame
column_names = df.columns.tolist()

# Assuming the last column is the target variable, and the rest are input variables
X = df[column_names[:-1]]  # Input variables
for i in range(5,8):
  y = df[column_names[i]]
  h=df.columns.values
  print("equation for ",h[i])
# Create and fit the Lasso regression model
  model = Lasso()
  model.fit(X, y)

    # Get the coefficients
  coefficients = model.coef_
  intercept = model.intercept_

    # Build the algebraic equation
  equation = "Target = "
  for i, col in enumerate(column_names[:-1]):
      equation += f"({coefficients[i]} * {col}) + "
  equation += str(intercept)

  print("Algebraic Equation:", equation)