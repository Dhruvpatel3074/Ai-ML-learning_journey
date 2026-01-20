# Working with JSON module

import json

data = {
    "name": "Dhruv",
    "course": "AI & ML",
    "year": 3
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("JSON Data:", loaded_data)
