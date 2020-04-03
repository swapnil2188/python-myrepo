#!/usr/bin/python

f = open("hosts.txt")

for i in f:
	name = i.split("\t", 1)
	print(name[0])

f.close()

