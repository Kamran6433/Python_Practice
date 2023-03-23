# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# My answer:
def find_average(numbers):
    answer = sum(numbers)/len(numbers)
    return answer

# Better answer by tachyonlabs:
def find_average(array):
    return sum(array) / len(array) if array else 0