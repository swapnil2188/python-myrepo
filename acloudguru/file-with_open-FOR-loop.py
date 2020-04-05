#!/usr/bin/python

print("\nOpen file and Read Line by Line using FOR loop")

with open("words") as input_file:
	for line in input_file:
		line = line.strip()
		if line[0] == 'w':
			print(line)	 
