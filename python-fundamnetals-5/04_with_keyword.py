# Using with keyword for file handling

with open("with_example.txt", "w") as file:
    file.write("Using with keyword is safe")

with open("with_example.txt", "r") as file:
    print(file.read())
