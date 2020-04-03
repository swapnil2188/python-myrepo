#!/usr/bin/python

import re

txt = "The Rain in Spain"

print "\nReturns a LIST containing JUST the ALL MATCHES\n"
x = re.findall("ai", txt)
print x
