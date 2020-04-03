#!/usr/bin/python

def convertToHM(mins):
	hours = mins / 60
	minutes = mins % 60
	return str(hours) + ':' + str(minutes)

print convertToHM(85)
