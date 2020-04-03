#!/usr/bin/python

birthday = {
  "Swap": "Ford",
  "Mom": "Mustang",
  "Anj": 1964
}

name = raw_input("We have birthday records of Swap, Mom, Anj ,Dad - Enter name: ")
print name
name1 = birthday.get(name)
print name1
