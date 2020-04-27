#!/usr/bin/python

import re

#s = input()
#s = str(s)

with open ("testdata") as f:
	for line in f:
		line = line.strip()
		x = re.search("Blues", line, re.IGNORECASE)
		if x:	
			print (x.string)
	
