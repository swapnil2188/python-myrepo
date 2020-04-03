#!/usr/bin/python

a = raw_input("Enter num 1: ")
print a
b = raw_input("Enter num 2: ")
print b
c = raw_input("Enter num 3: ")
print c

if a > b and a > c:
	print a, "is biggest"
elif b > a and b > c:
	print b, "is largest"
elif c > a and c > b:
	print c, "is largest"
