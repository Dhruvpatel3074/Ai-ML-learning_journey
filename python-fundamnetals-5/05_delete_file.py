# Deleting files using os module

import os

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("File deleted successfully")
else:
    print("File does not exist")
