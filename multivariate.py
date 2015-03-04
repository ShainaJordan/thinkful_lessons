import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
loansData.to_csv('loansData_clean.csv', header=True, index=False)

print list(loansData.columns.values)

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x.rstrip('%')) / 100)
loansData['Home.Ownership'] = loansData['Home.Ownership'].map(lambda x: x == "RENT")

intrate = loansData['Interest.Rate']
annual_inc = loansData['Monthly.Income']
home_ownership = loansData['Home.Ownership']

# The dependent variable
y = np.matrix(intrate).transpose()

# The independent variables shaped as columns
x1 = np.matrix(annual_inc).transpose()
x2 = np.matrix(home_ownership).transpose()

x = np.column_stack([x1,x2])

#Create a linear model
#The add_constant function simply builds the matrix with a first column initialized to ones for the intercept
income_ownership = sm.add_constant(x)

#Ordinary Least Squares is the simplest and most common estimator in which the two betas are chosen to minimize the square of the distance between the predicted values and the actual values. 
model = sm.OLS(y,income_ownership)
income_model = sm.OLS(y, x1)
income_ownership = sm.OLS(x1,x2)
f = model.fit()
g = income_model.fit()
h = income_ownership.fit()

print 'Coefficients with Income and Ownership are: ', f.params
print 'Intercept with Income and Ownership are: ', f.params
print 'P-Values with Income and Ownership are: ', f.pvalues
print 'R-Squared with Income and Ownership is: ', f.rsquared

print 'Coefficients with Income: ', g.params
print 'Intercept with Income: ', g.params
print 'P-Values with Income: ', g.pvalues
print 'R-Squared with Income: ', g.rsquared

print 'R-Squared for Income and Ownership: ', h.rsquared