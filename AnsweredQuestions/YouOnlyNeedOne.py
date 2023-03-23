# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

# My answer:
def check(seq, elem):
    for element in seq:
        if element == elem:
            return True
    return False

# Better answer by mstrfx:
def check(seq, elem):
    return elem in seq