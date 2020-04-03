#!/usr/bin/python

import re

string = raw_input("Enter the Search String: ")

#print (string)

f = open("testdata")

for i in f:
	x = re.search('string', i)
	print i
	#if x == True:
	#print (i)

f.close() 
