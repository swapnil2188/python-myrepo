#!/usr/bin/python

sen = list('Hello World Guys!!!!')


for w in sen:
 print w                    # print all characters

for w in range(0, len(sen)):
	sen[w]	= sen[w].lower()   # print all in lower case
print ''.join(sen)                 # string join func to join all chars

