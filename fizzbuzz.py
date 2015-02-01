n = 0 

while n <= 100:
	if n % 15 == 0:
		print "FizzBuzz because n = ", n
	elif n % 3 == 0:
		print "Fizz because n = ", n
	elif n % 5 == 0:
		print "Buzz because n = ", n
	else:
		print n, "because it's not Fizz or Buzz"
	n = n + 1