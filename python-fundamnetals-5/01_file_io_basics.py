# File I/O basics
# Writing and reading a simple text file

file = open("sample.txt", "w")
file.write("This is my first file handling program")
file.close()

file = open("sample.txt", "r")
content = file.read()
print("File content:", content)
file.close()
