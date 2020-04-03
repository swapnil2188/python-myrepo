#!/usr/bin/python

f=open("hosts.txt")

for line in f:
 #column = line.split("\t")
 x = slice(1)
 #col1 = column[0]
 #print (col1)
 print (line[x])
f.close()
