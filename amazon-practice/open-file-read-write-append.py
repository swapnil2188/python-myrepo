#!/usr/bin/python

#Default "rt" - no need to mention
f = open("myfile", "rt")

for line in f:
	print (line)

print "close the file after done processing\n"
f.close()

################
f1 = open("myfile", "r")

print "Open the file for Reading only\n"
print(f1.read())
f1.close()

f2 = open("myfile", "a")
print(f2.write("Appending\n"))
f2.close()

#This Below part Actually Overwrites the File - use append instead
f3 = open("myfile1", "w")
print(f3.write("Addingthis"))
f3.close()
