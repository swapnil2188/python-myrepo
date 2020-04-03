#!/usr/bin/python

s = "f++d+"

def SimpleSymbols(string):

 string = '=' + string + '='
 li = list(string)
 
 for i in range(0, len(li)):
		
	if li[i].isaplha():
		if li[i-1] != '+' or li[i+1] != '+':
			return 'false'
 
 return 'true'

#print SimpleSymbols(raw_input())
print SimpleSymbols(s)
