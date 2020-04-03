#!/usr/bin/python

sequence = [1,2,3,-1,3,4,5,-2]

for item in sequence:
	#Process all Positive items - Continue is SKIP item that doesnot fit the criteria
 if item > 0:
	print item
	continue

