#!/usr/bin/python

print "\n split into 16 items at first 16 spaces"

f = open("hosts_dump")
m = []

for line in f:
 m = line.split(" ", 16)        # print using Space as delimiter for all 16 Spaces- 17 Columns - Also add each line item as a LIST item 
 print m[16]                    # print the 16th index of a LIST
f.close		
