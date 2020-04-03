#!/usr/bin/python

def reverse_func(x):
 result = ""	
 for i in range(len(x),0,-1):
  result += x[i-1]
 return (result)

print reverse_func('swapnil')
