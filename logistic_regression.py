import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.to_csv('loansData_clean.csv', header=True, index=False)

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x.rstrip('%')) / 100)
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

#create a new column that evaluates if interest rate is above or below 12%
loansData['intRateEval'] = map(lambda x: x < .12, loansData['Interest.Rate'])
#loansData['intRateEval'] = loansData['Interest.Rate'] <=.12
intRateEval = loansData['intRateEval']

#create intercept column with value 1
loansData['Intercept'] = 1

loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
intercept = loansData['Intercept']

ind_vars = loansData[['Intercept', 'FICO.Score', 'Amount.Requested']]

logit = sm.Logit(loansData['intRateEval'], ind_vars)
result = logit.fit()

coeff = result.params
print coeff

#loanamt = 10000
#fico = 720

def logistic_function(intercept, fico, loanamt, coeff):
	p = 1/(1 + np.exp(coeff[0] + coeff[1]*(fico) + coeff[2]*(loanamt)))
	plt.plot(fico, p)

def inv_logistic_function(intercept, fico, loanamt, coeff):
	p_inv = 1/(1 + np.exp(-coeff[0] - coeff[1]*(fico) - coeff[2]*(loanamt)))
	plt.plot(fico, p_inv)

logistic_function(intercept, fico, loanamt, coeff)
inv_logistic_function(intercept, fico, loanamt, coeff)

plt.show()


