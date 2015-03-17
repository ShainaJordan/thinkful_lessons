import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansData = pd.read_csv('LoanStats3b.csv', header=True, low_memory=False)

# converts string to datetime object in pandas:
loansData['issue_d_format'] = pd.to_datetime(loansData['issue_d']) 
#created for different period
dfts = loansData.set_index('issue_d_format') 
#then have to convert to datetime

#create a timeseries
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

plt.plot(loan_count_summary)
plt.show()

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(loan_count_summary, lags=6, ax=ax1)

plt.show()

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(111)
fig = sm.graphics.tsa.plot_pacf(loan_count_summary, lags=6, ax=ax1)

plt.show()