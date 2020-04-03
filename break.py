#!/usr/bin/python

sequence = [1,2,3,-1,3,4,5,-2]

for item in sequence:
	#Press until first negative item - Break immediately out from last Condition/Match that qualifies - in this case firt -ve item
 if item < 0:
	print item
	break

