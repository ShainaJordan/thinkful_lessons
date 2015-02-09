import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print column_names

# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "The mean for the Alcohol dataset is:", df['Alcohol'].mean() 
# 5.4436363636363634
print "The median for the Alcohol dataset is:", df['Alcohol'].median() 
# 5.63
# If all numbers occur equally often, stats.mode() will return the smallest number
print "The mode for the Alcohol dataset is:", stats.mode(df['Alcohol'])[0]
# 4.02

print "The mean for the Tobacco dataset is:", df['Tobacco'].mean() 
# 3.6181818181818186
print "The median for the Tobacco dataset is:", df['Tobacco'].median() 
# 3.53 
print "The mode for the Tobacco dataset is:", stats.mode(df['Tobacco'])[0]
# 2.71

print "The range for the Alcohol dataset is:", max(df['Alcohol']) - min(df['Alcohol'])
# 2.4500000000000002
print "The standard deviation for the Alcohol dataset is:", df['Alcohol'].std() 
# 0.79776278087252406
print "The variance for the Alcohol dataset is:", df['Alcohol'].var() 
# 0.63642545454546284

print "The range for the Tobacco dataset is:", max(df['Tobacco']) - min(df['Tobacco'])
# 1.8499999999999996
print "The standard deviation for the Tobacco dataset is:", df['Tobacco'].std() 
# 0.59070835751355388
print "The variance for the Tobacco dataset is:", df['Tobacco'].var() 
# 0.3489363636363606