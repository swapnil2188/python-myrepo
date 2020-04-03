#!/usr/bin/python

num = 15
fib = [1,1]
i = 1 
while i < (num - 1):
	fib.append(fib[i] + fib[i-1])
	i += 1
print fib
