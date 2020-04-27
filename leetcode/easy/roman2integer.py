#!/usr/bin/python

roman_dict = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
roman = "XXLL"

sum = 0
prev = 0

for i in range(0, len(roman)):
    cur = roman_dict[roman[i]]
    if prev < cur:
        sum = sum - prev
        cur = cur - prev
    sum = sum + cur
    prev = cur
print (sum)
