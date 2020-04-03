#!/usr/bin/python

i = raw_input("Enter input")

r = i[::-1]

if i == r:
	print "Palindrome"
else:
	print "Not Palindrome"
