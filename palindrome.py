#!/usr/bin/python

n = input("Enter something: ")
n = str(n)
r = n[::-1]

if n == r:
	print ("Palindrome\n")
else:
	print ("NOT Palindrome\n")
	
