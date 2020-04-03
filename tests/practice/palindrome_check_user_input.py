#!/usr/bin/python

n = raw_input("Please enter your string: ")

i = n[::-1]

if n == i:
 print n, "is a Palindrome"
else:
 print n, "is not a palindrome"
