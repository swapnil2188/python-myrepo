#!/usr/bin/python

import re

txt = "The rain in Spain"
print "\nHere's the STRING in question"
print txt

x = re.search("\s", txt)

print "\n 1.Print the Start and End index position of the Match - using SPAN"
print (x.span())

print "\n 1.1 You can Also print just the Start or End Position of the match - Using start or stop"
print (x.start())

print "\n 2.Print the Entire String with the Match - using STRING"
print (x.string)

print "\n 3.Print Just the Matching part which is /\s here - using GROUP"
print (x.group())
