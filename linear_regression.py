import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x.rstrip('%')) / 100)
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()

# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

#Create a linear model
#The add_constant function simply builds the matrix with a first column initialized to ones for the intercept
X = sm.add_constant(x)
#Ordinary Least Squares is the simplest and most common estimator in which the two betas are chosen to minimize the square of the distance between the predicted values and the actual values. 
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params
print 'Intercept: ', f.params
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

for p in f.pvalues:
	if p <= .05:
		print "the pvalue is", p, "so this is a good model"
	else:
		print "the pvalue is", p, "so this is not a good model"





