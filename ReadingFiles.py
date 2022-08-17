# Reading files in Python is easy and effective.
# User is able to read any file in a computer using its absolute path.
# The open function is used to open a file by specifying the file name and the mode.

# The modes are as follows:
# "r" = read (default) | "r+" = read and write | "w" = write | "a" = append | "x" = create
# "t" = Text mode (default) | "b" = Binary mode

try:
    spotifyList = open("Spotify.txt", "r")
    try:
        print(spotifyList.readline())
        print(spotifyList.readlines(5))
        print(spotifyList.read(1000))
    except:
        print("Something went wrong reading the file.")
    finally:
        spotifyList.close()  # Its good practice to always close the file you opened.
except:
    print("Something went wrong opening the file.")


spotifyList = open("Spotify.txt", "r")
for i in spotifyList.read():  # This will print every single letter in every single item one by one (VERY LONG).
    print(i)

for i in spotifyList.readline():  # This will print every letter one by one of the first item in the file.
    print(i)

for i in spotifyList.readlines():  # this will print every item one by one.
    print(i)