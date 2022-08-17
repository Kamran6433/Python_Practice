# Sets in Python are another type of data structure which holds multiple data in one variable.
# A set is UNORDERED and UNINDEXED and DON'T ALLOW DUPLICATES.
# Sets are written with curly braces:

exampleSet = {1, 2, 8, 5, 1}
print(exampleSet)  # When this set is printed, the order of the set is random
                   # and the duplicate entries are removed.

# Sets can contain any data type adn a mix of data types.
mixedSet = {"Hello", 54, True, 9.88, True, "Metronomy The Look", "Hello"}
print(mixedSet)  # Again, the duplicate entries are not printed out.

print("----------UNION-----------")
# This method will Union (merge and remove duplicates) the two chosen sets together.
unionSet = mixedSet.union(exampleSet)
print(unionSet)