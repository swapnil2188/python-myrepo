#!/usr/bin/python

import re
import collections

with open("pg2009-darwin-1.txt") as f: 
    my_string = (" ".join(line.strip() for line in f)) 
    n = [] 
    n = re.split("\s", my_string) 
    m = [] 
    #print (n[0], n[1]) 
    for i in range(0, len(n), 3): 
        m.append([n[i],n[i+1],n[i+2]])
    print (m)	
    #counter = collections.Counter(m)
    #print (counter)
