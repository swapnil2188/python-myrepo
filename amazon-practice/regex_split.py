#!/usr/bin/python

import re

txt = "The Rain in Spain"

print "\nPrinting the string using SPLIT function as List\n"
x = re.split("\s", txt)
print x

print "\nSplitting the String at first SPACE using SPLIT and Printing the string as List\n"
x = re.split("\s", txt, 1)
print x
