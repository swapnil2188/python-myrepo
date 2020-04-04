#!/usr/bin/python

def product(numbers):
	p = 1
	for n in numbers:
		p *= n
	return p

print product([1,2,3,4])
