# Sets in Python are another type of data structure which holds multiple data in one variable.
# A set is UNORDERED and UNINDEXED and DON'T ALLOW DUPLICATES.
# Sets are written with curly braces:

exampleSet = {1, 2, 8, 5, 1, 54}
print(exampleSet)  # When this set is printed, the order of the set is random
                   # and the duplicate entries are removed.

# Sets can contain any data type adn a mix of data types.
mixedSet = {"Hello", 54, True, 9.88, True, "Metronomy The Look", "Hello"}
print(mixedSet)  # Again, the duplicate entries are not printed out.

print("----------UNION-----------")
# This method will Union (merge and remove duplicates) the two chosen sets together.
unionSet = mixedSet.union(exampleSet)
print(unionSet)

print("----------DIFFERENCE-----------")
# This method will find the Difference between the first set / second set or more sets.
differenceSet = mixedSet.difference(exampleSet)
print(differenceSet)

print("----------INTERSECTION-----------")
# This method will find the similarities between the first set / second set.
intersectionSet = mixedSet.intersection(exampleSet)
print(intersectionSet)

print("----------ISDISJOINT-----------")
# This method returns whether two sets have an intersection or not.
print(exampleSet.isdisjoint(mixedSet))

print("----------ISSUBSET-----------")
# This method returns whether another set contains this set or not.
copyExampleSet = {1, 2, 8, 5, 1, 54}
print(exampleSet.issubset(copyExampleSet))

print("----------ISSUPERSET-----------")
# This method returns whether this set contains another set or not.
print(exampleSet.issuperset(copyExampleSet))

print("----------UPDATE-----------")
# This method will add items from another set into the set that the function is being called by.
# The object in the update() method does not have to be a set.
# It can be any iterable object (tuples, lists, dictionaries etc.).
# WILL REMOVE DUPLICATES.
mixedSet.update(exampleSet)
print(mixedSet)

# THE METHODS IN LISTS CAN ALSO BE DONE IN SETS (POP, UPDATE, REMOVE ETC.)
