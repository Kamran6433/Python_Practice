# This file contains all teh string methods in Python. If I want to become a good programmer I must learn all the
# string methods for each language as they are all important to mastering the language.

text = "my name is Kamran and I will become a software engineer."

print("----------------------CAPITALIZE----------------------")
a = text.capitalize()
print("Text: " + text)
print("capitalize(): " + a)
# This method returns a string with the first character being capitalized.

print("----------------------CASEFOLD----------------------")
b = text.casefold()
print("Text: " + text)
print("casefold(): " + b)
# This method returns a string with all characters lower case.

print("----------------------CENTER----------------------")
c = text.center(100, "*")
print("Text: " + text)
print("center(): " + c)
# This method returns a string which is filled with the number of spaces specified with the string in the middle of
# the space. The second argument is what should be filled in for the space. Default is " ".

