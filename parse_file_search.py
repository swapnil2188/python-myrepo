#!/usr/bin/python

import re

print "USING SEARCH regex - Print the Matching items 'st11p01it-hpaj072046'\n\n"
print "WARNING DONT use SPLIT here WONT work as it PRINTs the List of ITEMS\n"

with open("hosts_dump") as f:
	for line in f:
 		line = line.strip()
		#m = re.search(r"\bMZCarrierBundle\b", line) 
		m = re.search(r"\bst11\w+-\w+", line)
		print(m.group())
