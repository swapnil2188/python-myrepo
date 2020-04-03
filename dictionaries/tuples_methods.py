#!/usr/bin/python

print "\n The count() method returns the number of times a specified value appears in the tuple"

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)
print x

print "\n The index() method finds the first occurrence of the specified value."
x = thistuple.index(8)
print x
