#!/usr/bin/python

print ("\nThis script handles multiple EXCEPTIONs - Excepts\n")
print ("If valid number TRY executes IF not VALID except part Executes\n")
print ("NameError as e: Print(e) can be used to Log errors from your script\n")

try:
	n = input("Enter a Valid number: \n")
	n1 = int(n)
	print("Valid Number: " + str(n1))
except ValueError:
	n = None
	print("That's not a Valid Number!")
except NameError as e:
	print("Something Wrong with your code! SYNTAX ERROR")
	print(e)
except:
	print("Not sure What went wrong")
else:
	print("Everything, Went as Planned - NO ERRORs!")
finally: 
	print("All DONE!")
