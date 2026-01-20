# Operations on files

file = open("data.txt", "w")
file.write("Python file operations")
file.close()

file = open("data.txt", "a")
file.write("\nAppending new line")
file.close()

file = open("data.txt", "r")
print(file.read())
file.close()
