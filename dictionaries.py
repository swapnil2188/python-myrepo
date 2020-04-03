#!/usr/bin/python

d = { 'name': 'daniel', 'age': 100 }   # Dictionary - KEY-VALUE

print d['age']    # Print the Value Using Key

items = d.items()
print items[0]

print d.keys()   # print All Keys
print d.values() # print All values


d['name'] = 'mike'    # Add/change the Value of existing key
print d.items()

if d.has_key('name'):    # Check if Key is in Dictionary if so add/Modify the Value
 d['name'] = 'swapnil'
else:
 d['name'] = 'mom'	 #If not Add the key-Value Pair

print d
