# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
# This file contains all teh string methods in Python. If I want to become a good programmer I must learn all the
# string methods for each language as they are all important to mastering the language.

text = "my name is Kamran and I will become a Söftware Engineer."

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
print("center(100, \"*\"): " + c)
# This method returns a string which is filled with the number of spaces specified with the string in the middle of
# the space. The second argument is what should be filled in for the space. Default is " ".

count = "COUNT"
print(count.center(60, "-"))
d = text.count("a", 2, 5)
print("Text: " + text)
print("count(\"a\", 2, 5): " + str(d))
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

endswith = "ENDSWITH()"
print(endswith.center(60, "-"))
f = text.endswith(".")
print("Text: " + text)
print("endswith(\".\"): " + str(f))
# This method returns true if the string starts with the specified value, otherwise false.
# The second argument is the position to start the search and the third argument is the position to end the search.

startswith = "STARTSWITH()"
print(startswith.center(60, "-"))
f = text.startswith("my")
print("Text: " + text)
print("startswith(\"my\"): " + str(f))
# This method returns true if the string starts with the specified value, otherwise false.
# The second argument is the position to start the search and the third argument is the position to end the search.

find = "FIND()"
print(find.center(60, "-"))
g = text.find("0", 10, 20)
print("Text: " + text)
print("find(\"0\", 10, 20): " + str(g))
# This method finds the first occurrence of the specified value. The method returns -1 if the value is
# not found. The method is almost the same as the index() method, the only difference is that the index() method
# raises an exception if the value is not found.
# The second argument is the position to start the search and the third argument is the position to end the search.

