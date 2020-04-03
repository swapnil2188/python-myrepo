#!/usr/bin/python

#Count
#Count how many times a character sequence occurs in a string. 
s = "hello world I am coding"
print s.count('o') #3

#Find
#Find the index at which the string appears in the original string
print s.find('world') #6
print s.find('mars') #-1

#isalpha and isdigit
# Determine if the string is alphabetic or if it is a digit
s = "hello"
n = "456"

print s.isalpha() # True
print s.isdigit() # False
print n.isdigit() # True

#Replace
v = "hello world"
print v.replace('world', 'mars') # Hello Mars

# Swapcase
# Swap all uppercase and lowercase characters.
print s.swapcase()

#title 
# Capitalize the first letter of each word
print s.title()

#join
#Join a list of strings into one string separated by the input string
nums = ['dan', 'mike', 'rob']

print ' '.join(nums) 
print '-'.join(nums)


# Upper and Lower
#Uppercase or lowercase a string

print s.upper()
print s.lower()
