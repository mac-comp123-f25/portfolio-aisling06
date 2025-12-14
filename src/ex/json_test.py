import json

person = {
    "name": "Aisling",
    "age": 18,
    "favorite_colors": ["green", "pink"],
    "is_student": True
}

print("Original Python dictionary:")
print(person)

json_string = json.dumps(person, indent=4)
print("\nConverted to JSON string:")
print(json_string)

loaded_data = json.loads(json_string)
print("\nConverted back to Python dict:")
print(loaded_data)
print("Name field from loaded data:", loaded_data["name"])

with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

print("\nJSON data written to person.json")

with open("person.json", "r") as f:
    file_data = json.load(f)

print("\nJSON data loaded from file:")
print(file_data)
