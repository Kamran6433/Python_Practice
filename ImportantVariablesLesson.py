# There are some special Python techniques with variables.

# You're able to assign values to multiple variables in one line:
a, b, c = 1, "She's a Rainbow", "The Rolling Stones"
print(a, b, c)

# You can also assign the same value to multiple variables.
d = e = f = "I am d, e and f"
print(d, e, f)

# An important thing with Python variables is that you're able to UNPACK a collection.
print("-----------------UNPACKING A COLLECTION-----------------")
books = ["Atomic Habits", "Mastery", "The One Thing"]
book0, book1, book2 = books
print(book0, book1, book2)

fav_fruits = ("Apple", "Mango", "Guava", "Pineapple", "Strawberry")

(green, *tropic, red) = fav_fruits
# The * is used to collect the rest of the list.

print("green: " + green)
print("tropic: " + str(tropic))
print("red: " + red)