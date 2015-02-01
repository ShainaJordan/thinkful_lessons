# Python program to display the Fibonacci sequence up to n-th term using recursive functions

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# take input from the user
nterms = int(input("How many terms? "))



# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print "The %d number in the Fibonacci sequence is: %d" %(nterms, recur_fibo(nterms))