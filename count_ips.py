#!/usr/bin/python

#SAMPLE LINE
#line = "Feb  6 20:11:56 router sshd[7156]: Failed password for root from 36.156.24.95 port 44362 ssh2"

print ("\nThis Script will Print the Count for IPs as a Dictionary using collections.Counter\n")

import re
import collections

with open("logfile") as in_file:
	lists = []
	for line in in_file:
		line = line.strip()
		if 'Failed' in line:
			if 'root' in line:
				m = re.search(r"\d+\.\d+\.\d+\.\d+", line)
				n = m.group()
				lists.append(n)
	counter = collections.Counter(lists)
	print (counter)
	print ("\n")	
