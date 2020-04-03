#!/usr/bin/python

def maxof3(x,y,z):
	if x > y and x > z:
	 return x, "is greater"
	elif y > x and y > z:
	 return y, "is greater"
	elif z > x and z > y:
	 return z, "is greater" 

a = raw_input("Enter first number: ")
b = raw_input("Enter second number: ")
c = raw_input("Enter third number: ")

print maxof3(a,b,c)
