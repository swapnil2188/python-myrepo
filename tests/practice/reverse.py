#!/usr/bin/python

#Take Arguments from Commandline and print reverse of all Arguments

import sys

length = len(sys.argv)
structure = str(sys.argv)

if length == 1:
	print "Pass Arguments"
	print "syntax: python reverse.py arg1 arg2"
else:
	print structure[::-1]

