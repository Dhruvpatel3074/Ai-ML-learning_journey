# Practice problem
# Count number of lines in a file

with open("lines.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3")

with open("lines.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))
