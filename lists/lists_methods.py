#!/usr/bin/python

print "\n append - The append() method appends an element to the end of the list"
fruits = ['apple', 'banana', 'cherry']
fruits.append("Orange")
print fruits

print "\n The clear() method removes all the elements from a list"
#fruits.clear()
#print (fruits)

print "\n The copy() method returns a copy of the specified list"
#x = fruits.copy()
#print (x)

print "\n The count() method returns the number of elements with the specified value"
x = fruits.count("cherry")
print (x)

print "\n The extend() method adds the specified list elements (or any iterable) to the end of the current list"
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print fruits

print "\n Returns the index of the first element with the specified value"

print "\n The insert() method inserts the specified value at the specified position"
fruits.insert(1, "GUAVA")
print fruits

print "\n The pop() method removes the element at the specified position"
print "default value is -1, which returns the last item ****IMPORTANT \n"
fruits.pop(1)
print fruits

print "\n The remove() method removes the first occurrence of the element with the specified value"
fruits.remove("apple")
print fruits

print "\n The reverse() method reverses the sorting order of the elements"
fruits.reverse()
print fruits

print "\n The sort() method sorts the list ascending by default."
print "sort Ascending reverse=FALSE (DEFAULT), sort Descending reverse=TRUE"
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print cars
#cars.sort(reverse=TRUE)
#print cars

#A function that returns the length of the value:
def myfunc(e):
 return len(e)

print "\n Sort Based on length of each item in List - smallest to largest"
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myfunc)
print cars
