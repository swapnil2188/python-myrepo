#!/usr/bin/python

pet_dict = {"dog": 3.5, "cat": 4.5, "parrot": 5.0, "mice": 2.5}

try:
	pet = input("Enter Pet: ")
	if pet in pet_dict.keys():
		print(pet_dict[pet])
except ValueError:
	pet = None
	print("Enter a Valid Pet!")	
except NameError:
	print("CHECK SYNTAX!")
else:
	print("All went as Planned!")
finally:
	print("All DONE!")
