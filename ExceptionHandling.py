# Exception handling is an important part of programming.
# It keeps the code base more structurally strong and secure
# Exception handling allows the user to make an error but not a fatal error.
# In Python, we use try and except instead of try and catch.
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as error:
    print(error)

# This is a simple try and except block of code which doesn't make use of the other things in exception handling.


try:
    num1 = int(input("Enter a number to divide with: "))
    num2 = int(input("Enter another number to divide with: "))
    answer = num1 / num2
except ZeroDivisionError as zDError:
    print(zDError)
except ValueError as vError:
    print(vError)
else:
    print(answer)
finally:
    print("This piece of code is finished running.")

# This piece of code makes use of all the blocks.
#
# The TRY block lets you test a block of code for errors.
#
# The EXCEPT block lets you handle the error.
#
# The ELSE block lets you execute code when there is no error.
#
# The FINALLY block lets you execute code, regardless of the result of the try- and except blocks.
