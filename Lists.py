nums = [9, 87, 22, 213, 0, 99, 73]
print(nums[0])

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
nums.sort()
print(nums)

# This function does what it says. It reverses the entire list.
nums.reverse()
print(nums)

# This function works with the stack, popping (removing) the LAST element unless an index is passed as an argument.
nums.pop()
print(nums)

# This function makes a copy of nums and returns a new list.
print(nums.copy())

# This function inserts a new value to a given index (index 1, in this example, is now 11010).
nums.insert(1, 11010)
print(nums)

# This function removes a given value in the list.
nums.remove(9)
print(nums)

# This function clears the entire list.
nums.clear()
print(nums)