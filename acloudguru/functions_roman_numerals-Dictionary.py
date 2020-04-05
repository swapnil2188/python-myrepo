#!/usr/bin/python

#Dictionary with all Roman numerals - Key -> Value Pairs
# No need for if conditions now or 2 functions like to_val

roman_dict = { "i" : 1, "v" : 5, "x" : 10, "l" : 50, "c" : 100, "m" : 1000 }

#Function to Convert the Roman Numerals to Values

def numerals(roman):
        total = 0
        prev = 0
        for i in roman:
                cur = roman_dict[i]
                if prev < cur:
                        total -= prev
                        cur -= prev
                total += cur
                prev = cur

        return total

print numerals("mmxvii")
