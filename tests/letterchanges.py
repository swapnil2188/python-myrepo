#!/usr/bin/python

#Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
#Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
#Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

#s = 'dhcnt' 								# INPUT STRING
s = 'swapnil'
s1 = list(s)								#Convert to list	

alphabet = "abcdefghijklmnopqrstuvwxyz"					# A-Z
alpha = list(alphabet)							# Convert to list

def LetterChanges(str):							#Function 
	lst = []
	for i in str:
		if i in alpha:
			a1 = alpha.index(i)
			lst.append(a1+1)				# We got index of next following letters to print
	lst1 = []
	for j in lst:
		a2 = alpha[j]
		if a2 == "a" or a2 == "e" or a2 == "i" or a2 == "o"  or a2 == "u": # Check for Vowels
			a3 = a2.upper()						   # Convert to UpperCase if vowel	
			lst1.append(a3)
		else:
			lst1.append(a2)						   #If not just append to same list			
	return lst1							#List of following letters 
print LetterChanges(s1)

