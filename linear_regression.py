import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x.rstrip('%')) / 100)

print loansData['Interest.Rate'][0:5]

loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

print loansData['Loan.Length'][0:5]

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

print loansData['FICO.Score'][0:5]

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()