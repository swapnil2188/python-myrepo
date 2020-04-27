#!/usr/bin/python

print ("Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.\n")

#You Enter Numbers or Letter 'raw_input' will handle Both as STRING#
inp = raw_input("Enter String:\n")

rv = inp[::-1]
if inp == rv:
  print (str(inp)+ " is a Palindrome\n")
else:
  print (str(inp)+ " is NOT a Palindrome\n")
