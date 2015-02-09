import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x.rstrip('%')) / 100)

print loansData['Interest.Rate'][0:5]

loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

print loansData['Loan.Length'][0:5]

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x]).values

print cleanFICORange
