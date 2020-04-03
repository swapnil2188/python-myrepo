#!/usr/bin/python

print "\n Create a new Empty file"
f = open("myfile.txt", "x")
#Create a new file if it does not exist
f = open("myfile.txt", "w")

#OPEN a file to WRITE to it

fout = open("foo.txt", "w")
fout.write("hello world")
fout.close()


#Append to an OPEN file

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

print "\n NOTE - You can only Open or append one at a time cant do both need to close/reopen file"
print "\n #open and read the file after the appending:"
f = open("demofile.txt")
print(f.read())
f.close()

#######Open the file "demofile3.txt" and overwrite the content ###
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

print "Remove the file demofile3.txt"
import os
os.remove("demofile.txt")



