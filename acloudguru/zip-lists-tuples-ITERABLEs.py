#!/usr/bin/python

fruits = ["Apple", "Orange", "Banana"]
veggies = ["Potato", "Tomato", "Onions"]

print (fruits)
print (veggies)

print ("\nZipping 2 Lists and Printing together\n")

for (f, v) in zip(fruits, veggies):
	print (f, v)

