#!/usr/bin/python

x = ('key1', 'key2', 'key3')
y = 0

print "\nThe fromkeys() method returns a dictionary with the specified keys and values"
thisdict = dict.fromkeys(x, y)
print(thisdict)

print "\nThe get() method returns the value of the item with the specified key"
x = thisdict.get("key1")
print x

print "\nThe items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list\n"

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["year"] = 2019
x = car.items()
print x

print "\nThe keys() method returns a view object. The view object contains the keys of the dictionary, as a list"
x = car.keys()
print x

print "\n just adding a new item car dictionary - The keys() method returns a view object. The view object contains the keys of the dictionary, as a list"

car["color"] = "white"
x = car.keys()
print x

print "\n values returns a list of all the values in the dictionary"
x = car.values()
print x

print "\n The pop() method removes the specified item from the dictionary"
x = car.pop("model")
print x
print car

print "\n The popitem() method removes the item that was last inserted into the dictionary"
car.popitem()
print car

print "\n The setdefault() method returns the value of the item with the specified key" 

print "\n The update() method inserts the specified items to the dictionary"
car.update({"color": "white"})
print (car)

print "\n join for dictionary"
myDict = {"name": "John", "country": "Norway"}
myseparator = "TEST"
x = myseparator.join(myDict)
print x
