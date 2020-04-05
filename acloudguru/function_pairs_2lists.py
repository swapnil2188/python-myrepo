#!/usr/bin/python

print ("\n Function Pairs that takes 2 lists and prints values side to side\n")

colors = ["red", "blue", "green"]
tops = ["Tshirt", "sweatshirt", "Hoodie"]

def pairs(c, t):
	lists = []
	for (i, j) in zip(c, t):
		lists.append((i,j))
	return lists

print pairs(colors, tops) 
