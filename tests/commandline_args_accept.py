#!/usr/bin/python

import sys

#print len(sys.argv)
#print str(sys.argv)

length = len(sys.argv)
#print length

if length == 1:
	print "Pass Arguments"
	print "syntax: python commandline_args_accept.py arg1 arg2"
else:
	print str(sys.argv)
