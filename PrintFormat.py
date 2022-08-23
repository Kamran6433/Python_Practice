# My beloved printf doesn't exist in Python... but it does.
# It exists as a function called format()

price = int(input("Enter a number:"))
string_to_format = "That'll be £{:.2f} for the starbucks tall iced latte (London price)."
print(string_to_format.format(price))

# You can add as many parameters to the format function.
# And add placeholders to make sure the format is done correctly.
# The numbers correspond to the parameters passed through and can be used more than once.
name = "Kamran"
age = 20
course = "Computer Science"
aspirations = "Software Engineer and Machine Learning expert"
text = "{0} is {1} years old and he studies {2} and wants to become a {3}.\n{0} is a wonderful student."
print(text.format(name, age, course, aspirations))

# Formatting Types
# Inside the placeholders you can add a formatting type to format the result:
#
# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format
