#!/usr/bin/python

def igpay(word):
	vowels = "aeiouAEIOU"
	if word[0] in vowels:
		return (word[0:] + "way")
	else:
		return (word[1:] + word[0] + "ay")

print igpay("swapnil")
