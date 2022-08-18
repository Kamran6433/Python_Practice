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