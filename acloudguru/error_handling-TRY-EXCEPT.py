#!/usr/bin/python

print ("\nThis script use ERROR Handling - TRY and EXCEPT\n")
print ("If valid number TRY executes IF not VALID except part Executes\n")

try:
	n = input("Enter a Valid number: \n")
	n1 = int(n)
	print("Valid Number: " + str(n1))
except ValueError:
	n = None
	print("That's not a Valid Number!\n")
