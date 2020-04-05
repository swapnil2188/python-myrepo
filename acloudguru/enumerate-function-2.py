#/usr/bin/python

haystack = []
haystack = ["Hay"] * 20
haystack[6] = "needle"

print haystack

for (i, v) in enumerate(haystack): 
    print ("Looking..") 
    idx = 0 
    if v == "needle": 
        idx = i 
        print ("FOUND it !! at Index = " + str(idx))
