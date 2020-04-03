#!/usr/bin/python

## returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]
print("banana" in x)

# returns True because a sequence with the value "pineapple" is not in the list
print("pineapple" not in x)

x = ["apple", "banana"]
y = ["apple", "banana"]

# returns False because x is not the same object as y, even if they have thew same content
print(x is y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x == y)

## returns True because x is not the same object as y, even if they have the same content
print (x is not y)

## to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print(x != y)
