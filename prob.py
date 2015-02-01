import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

# calculate the number of instances in the list
count_sum = sum(c.values())

#print the frequency distribution of numbers in test list
for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#create and print boxplot for test list
plt.boxplot(testlist)
plt.savefig("boxplot.png")

#create and print bar histogram for test list
plt.hist(testlist, histtype='bar')
plt.savefig("histogram.png")

#create and plot test list against random normal distribution
plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.savefig("normal_dist.png") 
