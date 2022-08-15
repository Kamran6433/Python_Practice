nums = [9, 87, 22, 213, 0, 99, 73]
print(nums[0])

strings = ["Kamran", "Hello", "Attack On Titan"]
print(strings[2])

# This lists contains different data types.
list_of_random_data_types = ["Car", 3.14, True, 1]
print(list_of_random_data_types)

# This list is a list of lists
list_of_lists = [nums, strings, list_of_random_data_types]
print(list_of_lists)

# ----------------------------------------------------------------

nums.sort()
print(nums)

nums.reverse()
print(nums)

nums.pop()
print(nums)

print(nums.copy())

nums.insert(1, 11010)
print(nums)

nums.remove(0)
print(nums)

nums.clear()
print(nums)