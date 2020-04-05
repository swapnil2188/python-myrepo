#!/usr/bin/python

#Function to Define the Value of each roman numeral symbol

def to_val(letter):
	if letter == "i": 
    	 return (1) 
	elif letter == "v":
    	 return (5) 
	elif letter == "x":
    	 return (10) 
	elif letter == "l":
    	 return (50) 
	elif letter == "c":
    	 return (100) 
	elif letter == "m":
	 return (1000)
	else:
	 return (0)

#Function to Convert the Roman Numerals to Values and Calling to_val from inside
#One function calling another Function

def numerals(roman):
	total = 0
	prev = 0
	for i in roman:
		cur = to_val(i)
		if prev < cur:
	 		total -= prev
	 	 	cur -= prev	
		total += cur
		prev = cur
	
	return total

print numerals("mmxlix")
