#!/usr/bin/python

myfile = open("foo.txt", "rt")

for i in myfile:
	print i
myfile.close()
