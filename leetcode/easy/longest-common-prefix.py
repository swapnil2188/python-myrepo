#!/usr/bin/python

print ("Longest Common Prefix in an array of words\n")

mylist =  ["flower","flow","float","flo"]
l = [len(st) for st in mylist]        # Get Lengths for each string in an array [6, 3, 5, 2]

lcp = ''
for i in range(min(l)):             # Scan from 1st letter to min string lengths
    tmp = [s[i] for s in mylist]    # Get i^th letter from each String in array tmp
    # print (tmp)
    # ['f', 'f', 'f', 'f']
    # ['l', 'l', 'l', 'l']
    # ['o', 'o', 'o', 'o']     #This will be print 4 lines each per letter if we have four common letters
    if min(tmp) == max(tmp):   # Check min and max meaning if F or L or O is in most of words
        lcp = lcp + tmp[0]     # Now append first letter of each Array(tmp) to string(lcp)
print (lcp)                    # Print longest common prefix String(lcp)
