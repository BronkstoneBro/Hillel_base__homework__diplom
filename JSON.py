import json

data = {
    123456: ("Arthur", 35),
    654321: ("John ", 25),
    123123: ("Bill", 22),
    456456: ("Dutch", 28),
    789789: ("Javier", 35)
}


with open("dictionary.json", "w") as json_file:
    json.dump(data, json_file)

print("save in file 'dictionary.json'")
