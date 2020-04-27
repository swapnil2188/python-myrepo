#!/usr/bin/python

a = [1,2,3,4,5]
n = len(a)-1

for i in range(0, n):
	o = a.pop(0)
	a.append(o)
	print (a)


