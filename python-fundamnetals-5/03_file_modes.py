# File modes in Python

file = open("modes.txt", "w")
file.write("Using write mode")
file.close()

file = open("modes.txt", "r")
print("Read mode output:", file.read())
file.close()
