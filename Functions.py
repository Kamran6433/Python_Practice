# Functions are really important in programming because it cuts down large chunks of code into smaller chunks.
# Functions are able to pass data through them and manipulate data through parameters.
# Functions need to be called to be executed otherwise they will be redundant.

def sum(x, y):
    return x + y


# Functions in Python need two lines of space after the last line because Python doesn't have curly braces to
# structure code. Instead, Python uses indentation.
print("Hello again world")
print(sum(67, 90))

# Functions are also built into languages such as the functions that are used for lists in Lists.py, and they make
# everything a lot more efficient and save a lot of time.

def raiseToThePower(base_number, power_number):
    result = 1
    for i in range(power_number):
        result = result * base_number
    return result


print(raiseToThePower(5, 2))