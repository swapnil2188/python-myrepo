#!/usr/bin/python

mylist = ["a","a","b","b",1,2,3,2,3,1]

mylist = list(dict.fromkeys(mylist))

print mylist
