#!/usr/bin/python

#SAMPLE LINE
#line = "Feb  6 20:11:56 router sshd[7156]: Failed password for root from 36.156.24.95 port 44362 ssh2"

import re								#Import REGEX module
import collections							#Import Collections module
	
file = open("logfile")							#Open input file	

mylist = []								#Declare Empty lists
mylist1 = []

for line in file:							#Every line in File	
	if re.search(r"\bFailed", line):				#If the matchobject exists in line
		if re.search(r"\broot", line):				#If the -#-#-#-#-#
			mylist = re.split(r"\s", line)			#Split the line at whitespaces and add it to mylist
			l = mylist[11]
			mylist1.append(l)				#Append each item to new list
			
counter=collections.Counter(mylist1)					#Counter is a dict subclass for counting hashable objects
print counter
file.close()
