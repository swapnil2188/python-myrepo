#!/usr/bin/python

ex ='This is sample file. This is not a sample file. Not a sample file'

def freq(str):
	
	# break the string into list of words 
	str_list = str.split()

	# gives set of unique words 
	unique_words = set(str_list)
	print unique_words
	
	for words in unique_words:
		print(words, str_list.count(words))

# calling the freq function
freq(ex)
