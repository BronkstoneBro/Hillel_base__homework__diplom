import json
import csv
import random

with open("dictionary.json", "r") as json_file:
    data = json.load(json_file)

with open('CSV_read.csv', 'w', newline="") as csv_file:
    option_open = ["ID", "Ім'я", "Вік", "Телефон"]
    writer = csv.DictWriter(csv_file, fieldnames=option_open)

    writer.writeheader()

    for id, person in data.items():
        name, age = person
        have_phone = random.choice([True, False])

        phone = ''
        if have_phone:
            numbers = ['095', '066', '098', '096', '050', '097']
            number = random.choice(numbers)
            phone_numbers = "".join(random.choice("0123456789")
                                    for _ in range(7))
            phone = f'{number}{phone_numbers}'

        writer.writerow({"ID": id, "Ім'я": name,
                         "Вік": age, "Телефон": phone})

print("save in CSV-file 'CSV_read.csv'")
