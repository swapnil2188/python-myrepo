#!/usr/bin/python

print ("\nOpen file using WITH OPEN as it will close the FILE when done")
print ("Will Also read the file as String\n")

with open("recipe.txt") as input_file:
	recipe = input_file.read()

print(recipe)
