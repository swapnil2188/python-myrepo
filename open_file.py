#!/usr/bin/python

#OPEN a file to read from it

fin = open("foo.txt")
f = open("demofile.txt", "rt")     
print "#Read mode and text format - are defaults"

for line in fin:
 print line
fin.close()
f.close()

#### Read contents of file ###
f = open("demofile.txt", "r")
print(f.read())

print(f.read(1))
print(f.readline())
