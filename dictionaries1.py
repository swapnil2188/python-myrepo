#!/usr/bin/python

# Code to check how many times each character appeared

s = "hello world aabbccc"
li = list(s)
d = {}

for c in li:
	if d.has_key(c):
		d[c] += 1
 	else:
		d[c] = 1

print d   # Print all dictinary

print d['a'] # Print for "A" only
