#!/usr/bin/python

#lists1 = [1,2,3,4]
#lists2 = [1,2,4,5]

print ("\nThis Function will return the Common elements amongst 2 Lists\n")
print ("Check INTERSECTION Inbuilt Function for Union of sets\n")

def intersect(lists1, lists2):
	lists3 = []
	for i in lists1:
		for j in lists2:
			if i == j:
		 		lists3.append(i)
	return lists3

print intersect([1,2,3,4], [1,2,4,5])
