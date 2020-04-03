#!/usr/bin/python

txt = "hello world world 123"

print "\n#capitalize"
x = txt.capitalize()
print (x)

print "\n#count"
y = txt.count("world")
print (y)

print "\n#endswith"
z = txt.endswith("123")
print (z)

print "\n#find"
a = txt.find("world")
print (a)

print "\n#index"
b = txt.index("123")
print (b)

print "\n#isalnum - all aplhanumeric"
c = txt.isalnum()
print (c)

print "\n#isalpha - alphabets only"
d = txt.isalpha()
print (d)

tuple = ("John", "Peter", "Swapnil")
print "\n#join - join all items in a string to form a String"
e = "_".join(tuple)
print (e)

text = "    banana  "
print "\n#lstrip - Remove all places to LEFT of string"
f = text.lstrip()
print('of all fruits', f, 'is my FAV')

print "\n#rstrip - Remove all places to RIGHT of string"
g = text.rstrip()
print("of all fruits", g, "is my FAV")

text = "I could eat bananas all day"
print "\n#partition - return as a Tuple after a match"
h = text.partition("bananas")
print (h)

text = "I could eat bananas bananas bananas all day"
print "\n#replace - replace one match with other value"
i = text.replace("bananas", "apples", 2)
print(i)

txt = "Mi casa, su casa."
print "\n#rfind - method finds the last occurrence of the specified value"
print "#rindex - SAME rfind == rindex"
j = txt.rfind("casa")
print(j)

txt = "apple banana cherry"
print "\n#rsplit - Split a string into a list, using space ( ) as the separator"
print "Convert a STRING -> LIST ******* IMPORTANT\n"
k = txt.rsplit(" ")
print (k)

txt = "welcome to jungle"
print "\n#split - Split a string into a list where each word is a list item"
l = txt.split()
print (l)

print "\n split into 2 items only OR at first space only"
m = txt.split(" ", 1)
print m

txt = "This is 1st sentence\n This is 2nd sentence"
print "\n Splitlines Split a string into a list where each line is a list item"
n = txt.splitlines()
print n

txt = "50"
print "\n zfill - Fill the string with zeros until it is 10 characters long"
o = txt.zfill(10)
print o
