import json


def list_comp(names, age):
    info = {k: v for (k, v) in zip(names, age)}
    return info


names = ["souhail", "Fati", "Zineb", "Mouad", "Abdo", "Fahd"]
age = [21, 15, 27, 30, 22, 18]

data = list_comp(names, age)


def database(data):
    for k, v in data.items():
        print(f"Name: {k:10}| Age: {v}")


database(data)

file_path = "Information.json"

with open(file_path, "w") as file:
    json.dump(data, file, indent=4)
    print(f"json file '{file_path}' was created")

with open(file_path, "r") as file:
    print(json.load(file))
