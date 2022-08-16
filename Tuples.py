# A Tuple is a data structure where you can store different values. Very similar to list.

# Tuples are created similarly to lists but instead of [] we use ()
# Lists are MUTABLE
# Tuples are IMMUTABLE which means unchanging over time or unable to be changed.
coordinates = (9, 3)
print(coordinates)

names = ("Harry", "Kamran")
print(names)

mix = (False, True, 89, 9.999, "Pelitia", False, False)
print(mix)

# you're also able to access all the indexes of the tuple using [] however you cannot MODIFY the tuple at any stage.

# the ONLY two functions you can use with tuples are:
print(mix.index(89))
print(mix.count(False))

# checking to see if 9.999 is contained in a tuple.
if 9.999 in mix:
    print("9.999 is in the tuple called mix")


# Since tuples are immutable, they cannot be changed however there is a workaround.
# You're able to turn the tuple into a list and change the elements before changing it back to a tuple.
x = (1, 2, 3, 4)
y = list(x)
y[0] = 10
x = tuple(y)
print(x)

# You're also able to join tuples together.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# You can also multiply tuples to make a larger tuple.
fruits = ("apple", "banana", "cherry", "carrot")
mytuple = fruits * 2

print(mytuple)