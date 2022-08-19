# Lists are a valuable data structure which can be easily mutated and changed for flexability.

nums = [9, 87, 22, 213, 0, 99, 73, 9, 9]
print(nums[0:]) # This colon simply means the rest.

strings = ["Kamran", "Hello", "Attack On Titan"]
print(strings[2])

# This lists contains different data types.
list_of_random_data_types = ["Car", 3.14, True, 1]
print(list_of_random_data_types)

# This list is a list of lists.
list_of_lists = [nums, strings, list_of_random_data_types]
print(list_of_lists)

# ----------------------------------------------------------------

# This function sorts the list in ascending order (Java programmers crying right now including me).
print("----------SORT-----------")
nums.sort()
print(nums)

# This function does what it says. It reverses the entire list.
print("----------REVERSE-----------")
nums.reverse()
print(nums)

# This function works with the stack, popping (removing) the LAST element unless an index is passed as an argument.
print("----------POP-----------")
nums.pop()
print(nums)

# This function counts how many elements of the same value are in the list (There are 1 elements that have the value 9)
print("----------COUNT-----------")
print(nums.count(9))

# This function makes a copy of nums and returns a new list.
print("----------COPY-----------")
print(nums.copy())

# This function inserts a new value to a given index (index 1, in this example, is now 11010).
print("----------INSERT-----------")
nums.insert(1, 11010)
print(nums)

# This function allows the user to add multiple elements to a list.
print("----------EXTEND-----------")
nums.extend([8, 888, 777, 999, 8])
print(nums)

# This function returns the index of first element with specified value (Works well with duplicate elements in a list)
print("----------INDEX-----------")
print(nums.index(8))

# This function adds to the end of the list
print("----------APPEND-----------")
nums.append(2222)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

# This function removes a given value in the list.
print("----------REMOVE-----------")
nums.remove(9)
print(nums)

# This function clears the entire list.
print("----------CLEAR-----------")
nums.clear()
print(nums)