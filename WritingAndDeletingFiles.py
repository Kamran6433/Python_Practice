import os
# In Python you're able to create files and write to them as well. (Even HTML files)
# Reading and writing files in Python is easy and effective.
# User is able to read and write any file in a computer using its absolute path.
# The open function is used to open a file by specifying the file name and the mode.

# The modes are as follows:
# "r" = read (default) | "r+" = read and write | "w" = write | "a" = append | "x" = create
# "t" = Text mode (default) | "b" = Binary mode

try:
    testFile = open("RandomTestFile.txt", "a")
    try:
        okay = int(input("Enter random numbers to add to the file: "))
    except ValueError as valueError:
        print(valueError)
    else:
        testFile.write(str(okay) + "\n")
        print(str(okay) + "Has been added to RandomTestFile.txt")
    finally:
        testFile.close()
except:
    print("something went wrong with opening RandomTestFile.txt")


# There is a way to delete files in Python, but first you must import OS.
# Check if file exists, then delete it:

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")