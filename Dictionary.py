# Dictionaries are a data structure that stores data in key: value pairs.
# Dictionaries are written with {}.
# Dictionary items are ORDERED, MUTABLE but does not allow duplicates.
dict = {
    1: "car",
    2: "house",
    3: "dog"
}
# Accessing dictionary elements can be done by:
print(dict[1])
# or:
print(dict.get(3))

# To get the length of a dictionary you can use the len function.
# **Notice how the length of the dictionary is referring to the pairs and NOT the keys and values individually.**
print(len(dict))

# You're able to mix and match different data types in dictionaries.
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    list: ["red", "white", "blue"],
    1: 26.9877
}
print(thisdict)


# There's a method called keys() that returns a list of all the keys in the dictionary.
print(thisdict.keys())

# Similarly there's a method called values() that returns a list of all the values in the dictionary.
print(thisdict.values())

# The items() method will return each item in a dictionary, as tuples in a list.
print(thisdict.items())


# To update elements in the dictionary, you cna use the update() method or simply access the key and change the value.
thisdict["year"] = 2018
# or by using the update() function and passing a dictionary as an argument using {}. The update() method will
# replace the given key with the new value but if there's no key that matches it will simply add it on.
thisdict.update({"year": 2000})
thisdict.update({"Hello": "World"})
print(thisdict)

# Nested dictionaries exist as well.
nestedDict = {
    "thisdict": thisdict,
    "dict": dict
}
print(nestedDict)