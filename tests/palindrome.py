#!/usr/bin/python

s = raw_input("Enter a string: ")
print s
r = s[::-1]

if r == s:
	print "IT is a Palindrome"
else:
	print "NOT palidrome"
