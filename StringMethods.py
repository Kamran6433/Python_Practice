# This file contains all teh string methods in Python. If I want to become a good programmer I must learn all the
# string methods for each language as they are all important to mastering the language.

text = "my name is Kamran and I will become a söftware engineer."

capitalize = "CAPITALIZE"
print(capitalize.center(60, "-"))
a = text.capitalize()
print("Text: " + text)
print("capitalize(): " + a)
# This method returns a string with the first character being capitalized.

casefold = "CASEFOLD"
print(casefold.center(60, "-"))
b = text.casefold()
print("Text: " + text)
print("casefold(): " + b)
# This method returns a string with all characters lower case.

center = "CENTER"
print(center.center(60, "-"))
c = text.center(100, "*")
print("Text: " + text)
print("center(): " + c)
# This method returns a string which is filled with the number of spaces specified with the string in the middle of
# the space. The second argument is what should be filled in for the space. Default is " ".

count = "COUNT"
print(count.center(60, "-"))
d = text.count("a", 2, 5)
print("Text: " + text)
print("count(): " + str(d))
# This method returns the number of times a specified value appears in the string.
# The second argument is the position to start the search and the third argument is the position to end the search.

encode = "ENCODE"
print(encode.center(60, "-"))
# Parameter	            Description
# encoding	            Optional. A String specifying the encoding to use. Default is UTF-8
# errors	            Optional. A String specifying the error method. Legal values are:
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	            - ignores the characters that cannot be encoded
# 'namereplace'	        - replaces the character with a text explaining the character
# 'strict'	            - Default, raises an error on failure
# 'replace'	            - replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character
e = text.encode(encoding="ascii", errors="namereplace")
print("Text: " + text)
print(e)
# This method encodes the string, using the specified encoding (default: UTF-8).

endswith = "ENDSWITH"
print(endswith.center(60, "-"))
f = text.endswith(".")
print("Text: " + text)
print("count(): " + str(f))
# This method returns true if the string ends with the specified value, otherwise false.
# The second argument is the position to start the search and the third argument is the position to end the search.

find = "FIND"
print(find.center(60, "-"))
g = text.find("0", 10, 20)
print("Text: " + text)
print("count(): " + str(g))
# This method finds the first occurrence of the specified value. The method returns -1 if the value is
# not found. The method is almost the same as the index() method, the only difference is that the index() method
# raises an exception if the value is not found.
# The second argument is the position to start the search and the third argument is the position to end the search.
