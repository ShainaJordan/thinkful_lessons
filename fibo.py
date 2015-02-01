#Define the function for the Fibonacci algorithm

def F(n):
    if n < 2:
       	return n
    else:
    	print "the function is iterating through the %d function" %(n)
       	return (F(n-2) + F(n-1))
       	
n = 8
print "The %d number in the Fibonacci sequence is: %d" %(n, F(n))