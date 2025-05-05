# Project one: taking an input from terminal and saving it as a file in the folder

import sys

# the data variable will store all the information typed on the command line after the name of the file
data = sys.argv[1:]

# this will print the data back to the user
print("This is your data: ", data)

# this will open a new file called 'file.txt' in the writing mode
new_file = open("file.txt", "w")

# this will write new things to the data already present in the file, that is it will simply join
new_file.write(" ".join(data))

# the written file will then be closed
new_file.close()

# new commits
