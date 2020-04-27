#!/usr/bin/python

print ("Function to Find a number in an array and print as YES/NO\n")

def findNumber(arr, k): 
    for i in range(0, len(arr)):
        n = arr[i] 
        if k == n: 
            print ("YES")
        else: 
            print ("NO")

findNumber([1,2,3,4,5], 4)

