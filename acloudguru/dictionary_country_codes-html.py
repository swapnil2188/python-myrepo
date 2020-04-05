#!/usr/bin/python

#Script to Print the Map-Dictionary of Country Codes

countries = { "Al": "Albania", 'DZ': "Algeria", 'IN': "India", 'US': "USA" }

for (code, country) in countries.items():
	print('<option value="{0}">{1}</option>'.format(code, country))

