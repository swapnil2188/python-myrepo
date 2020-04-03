#!/usr/bin/python

# Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence 
# by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them 
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. 
# The string will not be empty and will have at least one letter. 

#s = "+d+=3=+s+" 					# INPUT 
s = "f++=d+"
s1 = list(s)						#Input string to list	

alphabet = 'abcdefghijklmnopqrstuvwxyz'			#check if a letter 
alpha = list(alphabet)

def SimpleSymbols(str): 
	counter = 0
	counter1 = 0
	counter2 = 0
	for index, i in enumerate(s1):			# Use Enumerate inbuilt function
		#a1 = (index, i)			# Print Index and Value
		if i in alpha:
			counter += 1
			a1 = s1[index + 1]		# Printing index after letter 
			a2 = s1[index - 1]		# Printing index before letter
			if a1 == '+' and a2 == '+':	# Check for before after '+'
				counter1 += 1
		elif i == '+':
			counter2 += 1						
	if (counter == counter1 and counter2  % 2 == 0): # If we have odd + signs or no. of letters =! +signs we say false
		return True		 
	else:
   	 	return False 

# keep this function call here  
print SimpleSymbols(s) 
