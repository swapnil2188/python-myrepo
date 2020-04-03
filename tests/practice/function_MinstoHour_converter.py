#!/usr/bin/python

def convertMintoHour(mins):
	hours = mins / 60
	minutes = mins % 60
	return str(hours) + ':' + str(minutes)

print convertMintoHour(55)
