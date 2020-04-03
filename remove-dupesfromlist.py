#!/usr/bin/python

mylist = ["a", "b", "c", "a", "a", "c"]
mylist = list(dict.fromkeys(mylist))
print mylist
