#!/usr/bin/python

words = ['apple', 'orange', 'banana']

with open('scrabble.txt', 'a') as output_file:
	for word in words:
		output_file.write(word + "\n")
