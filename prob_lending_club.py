import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

# Split each item in this list on the commas
data = [i.split(', ') for i in loansData] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

#create and save boxplot for amount requested
loansData.boxplot(column='Amount.Requested')
plt.show()

#create and save boxplot for amount funded
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

#create and save histogram for amount requested
loansData.hist(column='Amount.Requested')
plt.show()

#create and save histogram for amount funded
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()



plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
