#!/usr/bin/python

def square(li):
	newlist = []
	for i in range(0,len(li)):
		result = li[i] * li[i]
		newlist.append(result)
	return newlist

print square([1,2,3,4])
