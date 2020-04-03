#!/usr/bin/python

import re

txt = "The Rain in Spain"

print "\nReplacing ALL Spaces with 7 using SUB function in string\n"
x = re.sub("\s", "7", txt)
print x

print "\nReplacing 1st Space ONLY with 7 using SUB Function in string\n"
x = re.sub("\s", "7", txt, 1)
print x
