#!/usr/bin/python

from collections import Counter

input = "This is sample file. This is not a sample file. Not a sample file"

def find_dup_char(input):
	# now create dictionary using counter method which will have strings as key and their frequencies as value
	WC = Counter(input)
	j = -1
	#print WC

	# Finding no. of occurrence of a character and get the index of it.
	for i in WC.values():
		j = j + 1
		if( i > 1 ):
			print WC.keys()[j],
#Call the Function
find_dup_char(input)				 
