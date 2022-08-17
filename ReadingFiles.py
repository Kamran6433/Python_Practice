# Reading files in Python is easy and effective.
# User is able to read any file in a computer using its absolute path.
# The open function is used to open a file by specifying the file name and the mode.

# The modes are as follows:
# "r" = read (default) | "r+" = read and write | "w" = write | "a" = append | "x" = create
# "t" = Text mode (default) | "b" = Binary mode

spotifyList = open("Spotify.txt", "r")
print(spotifyList.read(1000))
spotifyList.close()




