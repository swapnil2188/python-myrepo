#!/usr/bin/python

string = 'Hello World I am Swapnil'


print string[5:15:1]		# [START:END:STEP]
print string[5:15:2]		# [PRINT every 2 character]

print string[::-1]		# Reversing a string

print len(string)

print string.isdigit()		#isdigit function to confirm if its a digit or NOT

num = '77'
print num.isdigit()		#Will return True for integer

#print num.isnumeric()		# Similar function

lookfor = 'World'

print string.find(lookfor)	#FIND function to looks for world

print string[string.find(lookfor):] #Printing Everything from World to End
print string[string.find(lookfor):15] #Printing Everything from upto 15th Index  	

print string.title()		#Make all first letter Caps

print list(string)		#String to list convert

string = string.upper()		#Function to convert UpperCase
print string.isupper()		#Returns True

print string.swapcase()		#Swap the case for every character
