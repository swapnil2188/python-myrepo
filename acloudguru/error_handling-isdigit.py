#!/usr/bin/python

print ("\nUsing isdigit BuildIn STRING Function to check if INPUT is num\n")
print ("Note - This Function will only work on strings hence str(n)\n")

n = input("Enter a Valid Number: \n")
n = str(n)

if not n.isdigit():
	print("Enter a valid number: \n")
else:
	print(str(n) + " is a Valid Number\n")
