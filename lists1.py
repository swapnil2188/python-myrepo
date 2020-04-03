#!/usr/bin/python

li = [1, 2, 3, -10, 'hello', True]

print li

print "Printing Length of a list"
print len(li)

print "Printing Minimum value of a list"
print min(li)

print "Printing Max value of a list"
print max(li)

lst = [1, 2, 3, 45, 2000]

print lst

print "Appending value -2" 
lst.append(-2)
print lst

print "REMOVE Delete POP LAST Element from a List"
lst.pop()    # REMOVE/Delete/POP LAST Element from a List
print lst

print "Insert a at Index 0 in list"
lst.insert(0, 'a')   #Insert a at Index 0 in list
print lst

print "Remove a specific element" 
lst.remove(2) 		#Remove a specific element
print lst # [1, 3]

print "Print Index of Value 3"
print lst.index(3)  #Print Index of a Value
