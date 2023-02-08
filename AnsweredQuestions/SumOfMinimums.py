# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.

# For Example:

# [ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
# , [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
# , [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
# ]
# So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.

# Note: You will always be given a non-empty list containing positive values.

def sum_of_minimums(numbers):
    answer = 0
    min = 100000
    for rows in range(len(numbers)):
        for number in range(len(numbers[rows])):
            if numbers[rows][number] < min:
                min = numbers[rows][number]
        answer += min
        min = 100000
                
    return answer

# Better answer by g.jay.hewitt:

def sum_of_minimums(numbers):
    total = 0
    for nums in numbers:
        total += min(nums)
    return total

# Best answer by Unnamed:

def sum_of_minimums(numbers):
    return sum(map(min, numbers))