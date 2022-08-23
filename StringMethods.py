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
# ljust()	Returns a left justified version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# translate()	Returns a translated string
# zfill()	Fills the string with a specified number of 0 values at the beginning

# This file contains all the string methods in Python. If I want to become a good programmer I must learn all the
# string methods for each language as they are all important to mastering the language.

text = "#|my name is, Kamran, and I will become a, Söftware Engineer specialising in AI.[][##||"

capitalize = "CAPITALIZE"
print(capitalize.center(60, "-"))
a = text.capitalize()
print("Text: " + text)
print("capitalize(): " + a)
print()
# This method returns a string with the first character being capitalized.

casefold = "CASEFOLD"
print(casefold.center(60, "-"))
b = text.casefold()
print("Text: " + text)
print("casefold(): " + b)
print()
# This method returns a string with all characters lower case.

center = "CENTER"
print(center.center(60, "-"))
c = text.center(100, "*")
print("Text: " + text)
print("center(100, \"*\"): " + c)
print()
# This method returns a string which is filled with the number of spaces specified with the string in the middle of
# the space. The second argument is what should be filled in for the space. Default is " ".

count = "COUNT"
print(count.center(60, "-"))
d = text.count("a", 2, 5)
print("Text: " + text)
print("count(\"a\", 2, 5): " + str(d))
print()
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
print()
# This method encodes the string, using the specified encoding (default: UTF-8).

endswith = "ENDSWITH()"
print(endswith.center(60, "-"))
f = text.endswith(".")
print("Text: " + text)
print("endswith(\".\"): " + str(f))
print()
# This method returns true if the string starts with the specified value, otherwise false.
# The second argument is the position to start the search and the third argument is the position to end the search.

startswith = "STARTSWITH()"
print(startswith.center(60, "-"))
g = text.startswith("my")
print("Text: " + text)
print("startswith(\"my\"): " + str(g))
print()
# This method returns true if the string starts with the specified value, otherwise false.
# The second argument is the position to start the search and the third argument is the position to end the search.

find = "FIND()"
print(find.center(60, "-"))
h = text.find("a", 10, 20)
print("Text: " + text)
print("find(\"0\", 10, 20): " + str(h))
print()
# This method finds the first occurrence of the specified value. The method returns -1 if the value is
# not found. The method is almost the same as the index() method, the only difference is that the index() method
# raises an exception if the value is not found.
# The second argument is the position to start the search and the third argument is the position to end the search.

rfind = "RFIND()"
print(rfind.center(60, "-"))
i = text.rfind("a", 10, 20)
print("Text: " + text)
print("rfind(\"0\", 10, 20): " + str(i))
print()
# This method finds the last occurrence of the specified value. The method returns -1 if the value is
# not found. The method is almost the same as the index() method, the only difference is that the index() method
# raises an exception if the value is not found.
# The second argument is the position to start the search and the third argument is the position to end the search.

myTuple = ("Kamran", "Is", "Excellent")
join = "JOIN()"
print(join.center(60, "-"))
j = "#".join(myTuple)
print("Text: " + text)
print("\"#\".join(myTuple): " + j)
print()
# This method takes all items in an iterable (List, Tuple, Set, Dictionary) and joins them into one string.

lower = "LOWER()"
print(lower.center(60, "-"))
k = text.lower()
print("Text: " + text)
print("lower(): " + k)
print()
# This method returns a string where all the characters are lower case.

upper = "UPPER()"
print(upper.center(60, "-"))
l = text.upper()
print("Text: " + text)
print("upper(): " + l)
print()
# This method returns a string where all the characters are upper case.

split = "SPLIT()"
print(split.center(60, "-"))
m = text.split(",", 5)
print("Text: " + text)
print("split(\",\", 5): " + str(m))
print()
# This method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# You can also specify how many lists you want (maxsplit).

rsplit = "RSPLIT()"
print(rsplit.center(60, "-"))
n = text.rsplit(",", 5)
print("Text: " + text)
print("rsplit(\",\", 5): " + str(n))
print()
# This method splits a string into a list, starting from the right.
# You can specify the separator, default separator is any whitespace.
# You can also specify how many lists you want (maxsplit).

splitlines = "SPLITLINES()"
print(splitlines.center(60, "-"))
n = text.splitlines()
print("Text: " + text)
print("splitlines(): " + str(n))
print()
# This method splits a string into a list. The splitting is done at LINE BREAKS.

replace = "REPLACE()"
print(replace.center(60, "-"))
o = text.replace(",", " HAHAHAH ", 2)
print("Text: " + text)
print("replace(\",\"): " + str(o))
print()
# This method replaces a specified phrase with another specified phrase.
# The first argument is the phrase you want to replace with the second argument.
# The third argument is how many times you want it replaced.

strip = "STRIP()"
print(strip.center(60, "-"))
p = text.strip("#][|")
print("Text: " + text)
print("strip(\"#][|\"): " + str(p))
print()
# This method removes any leading (spaces at the beginning) and trailing (spaces at the end)
# characters (space is the default leading character to remove).

lrstrip = "L + RSTRIP()"
print(lrstrip.center(60, "-"))
q = text.lstrip("#][|")
r = text.rstrip("#][|")
print("Text: " + text)
print("lstrip(\"#][|\"): " + str(q))
print("rstrip(\"#][|\"): " + str(r))
print()

swapcase = "SWAPCASE()"
print(swapcase.center(60, "-"))
s = text.swapcase()
print("Text: " + text)
print("swapcase(): " + s)
print()
# This method returns a string where all the upper case letters are lower case and vice versa.

title = "TITLE()"
print(title.center(60, "-"))
t = text.title()
print("Text: " + text)
print("title(): " + t)
print()
# This method returns a string where the first character in every word is upper case.
