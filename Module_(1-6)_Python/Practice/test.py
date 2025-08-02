import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Data from JSON file:")
print(json.dumps(data, indent=4))
