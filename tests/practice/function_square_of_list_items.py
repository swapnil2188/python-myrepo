#!/usr/bin/python

#[1, 2, 3, 4] - Input
#[1, 4, 9, 16] - Output

def square(li):
 newList = []
 for i in range(0, len(li)):
  result = li[i] * li[i]
  newList.append(result)
 return newList 

print "your Input has to be a List"
print square([1,2,3,4])
