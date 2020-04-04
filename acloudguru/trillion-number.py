#!/usr/bin/python

n = 1000000000000
m = 100
d = 1

for i in range(1, n, d):
	d = i * i			#Step by Square of number to ITERATE real quick
	if d >= n:
		print (str(d) + " Found at Index " + str(i))
		break 
