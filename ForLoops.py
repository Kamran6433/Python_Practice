# Practicing for loops and tinkering with it to learn it in Python.
listOfRandomObjects = ["Plane", "Laptop", "Credit Card", "Blue Whale", "Binary Search", "Curry"]

for i in listOfRandomObjects:
    print(i)


for i in "Supercalifragilisticexpialidocious":
    print(i)


for i in range(10):
    print(i)


# You're able to use the range function and the len function to iterate through the length of a list or data structure.
for i in range(len(listOfRandomObjects)):
    listOfRandomObjects[i] = None


print(listOfRandomObjects)

# You're also able to put more parameters in the range function:
for i in range(0, 100, 5): # range(Start, End, Incrementation)
    print(i)
else:
    print("Finished looping!")
# We're also able to add an else statement to execute code when the loop is completed.


# Last but not least, we can nest for loops for complex or multidimensional iterations.
simpleList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
simpleList2 = [10, 20, 30, 40, 50]
for x in simpleList1:
    for y in simpleList2:
        print(x, y)