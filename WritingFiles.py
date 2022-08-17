# In Python you're able to create files and write to them as well. (Even HTML files)
# Reading and writing files in Python is easy and effective.
# User is able to read and write any file in a computer using its absolute path.
# The open function is used to open a file by specifying the file name and the mode.

# The modes are as follows:
# "r" = read (default) | "r+" = read and write | "w" = write | "a" = append | "x" = create
# "t" = Text mode (default) | "b" = Binary mode

testFile = open("RandomTestFile.txt", "a")
okay = input("Enter a name and random description to add to the file: ")
testFile.write(okay + "\n")