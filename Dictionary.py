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