#!/usr/bin/python

print "Fibonacci is Addition of last 2 numbers gives you next number and so on."
print "Example 1,1,2,3,5,8,13.."

def fib():
	count = int(raw_input("How many fibonacci numbers you need?: "))
	i = 1
	if count == 0:
		fib = []
	elif count == 1:
		fib = [1]
	elif count == 2:
		fib = [1,1]
	elif count > 2:
		fib = [1,1]
		while i < (count - 1):
			fib.append(fib[i] + fib[i-1])
			i += 1
	return fib
print(fib())
raw_input()	
