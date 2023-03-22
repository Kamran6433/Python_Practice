# Using the language of your choice, write a program that can evaluate if a string
# (provided by the user) that contains a sequence of bracket characters is “balanced” or not.
# Example of balanced string: ‘[{[]}()]’
# Example of string that is not balanced: ‘{[(])}’
# Your program/function can be a command line or terminal app, a web application, Jupyter Notebook, or in any form you like.
# The function should take a string containing brackets, e.g. ‘({[]})’,
# as a parameter - this can be from a file, on the command line, or an interactive prompt.
# The function should return a Boolean (string), where ‘true’ represents a balanced string and ‘false’ represents a string that is not balanced.
# Test myself.


def balanced_string(string):

    # Here I check if the string is empty which means I don't have to enter a loop to check if its empty.
    if not string or len(string) % 2 != 0:
        return False

    # Initialise a stack as a list in Python. The reason why I use a stack data structure is because
    # I'm able to keep track of the previous character that has been added to the stack and
    # pop from the stack if there is a matching closing character.

    stack = []



    # character contains the current character in the string to evaluate.
    for character in string:
        if character in ["[", "{", "("]:
            # If there is an opening character I push to the stack.
            stack.append(character)
        else:
            if not stack:
                return False
                # Else it would be a closing character in which case I check which closing character it is.
            previous_character = stack.pop()
                # But before I check the closing character
                # I must retrieve the previous character by removing and storing the last character using pop()
            if previous_character == "[":
                if character != "]":
                    return False

            if previous_character == "{":
                if character != "}":
                    return False

            if previous_character == "(":
                if character != ")":
                    return False

    # This checks to see if the stack is empty or not.
        # If the stack is empty it means all the opened brackets have been popped
        # from the stack and the corresponding closing brackets match meaning the string is balanced
    if not stack:
        return True
    else:
        return False


if __name__ == "__main__":

    # My test cases
    # True
    # False
    # True
    # False
    # False
    # False
    # True
    # False
    # True
    # False
    # True
    # False
    # False
    strings = ["{}", "{[}", "[[]]", "{{{]{]", "[}", "{{{{{{}}}}}", "[{[]}()]", "{[(])}", "{}[]()", "{}{}{}{}}", "({{[]}})", "{{{{", "]))}", "{}))"]
    # True
    # False
    # True
    # False
    # False
    # False
    # True
    # False
    # True
    # False
    # True
    # False
    # False

    for string in strings:
        # The nature of the function is to look for unbalanced and return False as early as possible.
        # The only instance when the function returns true is when it passes through all the
        # false evaluations.
        if not balanced_string(string):
            print("False")
        else:
            print("True")
