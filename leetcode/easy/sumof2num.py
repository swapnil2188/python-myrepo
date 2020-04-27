#!/usr/bin/python

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

nums = [2,7,11,15]
target = 9

print ("\n##Solution-1 #Brute Force - For in For\n")

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] != nums[j]:
            if nums[i] + nums[j] == target:
                print (nums[i], nums[j])
print ("Solution-1 Time complexity is O(n^2)\n")

print ("\n\n#### Solution-2 #### Hashes\n")
mydict = {}
for i in range(len(nums)):
    diff = target-nums[i]
    if(diff in mydict):
        index = mydict[diff]
        print (index, i)
    else:
        mydict[nums[i]] = i
print (mydict)

print ("\nSolution-2 Time complexity is O(n) but Space complexity is Higher as hashes take more space\n")

###### EXPLANATION ####
#iter1 #i = 0
#diff = 9-2 = 7
#if FALSE since mydict is empty
#else
#  so in mydict add key [num[i]] which is 2 and value index i(0)
#dict = [2:0]

#iter2 #i = 1
#diff = 9-7 = 2
#if TRUE as Dict has 2 in it#
#  index = mydict[diff] (mydict[2]) = 0
#  print (index, i) = (0, 1)
#else FALSE

#iter3 #i = 2
#diff = 9-11 = -2
#if FALSE since not present
#else
#  so in mydict add key [num[i]] which is 11 and value index i(2)
#dict = [2:0, 11:2]

#iter4 #i = 3
#diff = 9-15 = -6
#if FALSE since not present
#else
#  so in mydict add key [num[i]] which is 15 and value index i(3)
#dict = [2:0, 11:2, 15:3]

######
