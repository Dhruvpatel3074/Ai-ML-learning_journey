# finally keyword example

try:
    file = open("finally.txt", "w")
    file.write("Testing finally block")
finally:
    file.close()
    print("File closed successfully")
