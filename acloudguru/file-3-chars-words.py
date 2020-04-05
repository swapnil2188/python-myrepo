#!/usr/bin/python

print("Printing all Lines with length greater than 3")

with open("words") as input_file:
	for line in input_file:
		line = line.strip()
		if len(line) < 4:
			continue
		if line[0] == 'a':
			print (line)
