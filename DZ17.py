line1 = input("Введіть перший рядок: ")
line2 = input("Введіть другий рядок: ")
line3 = input("Введіть третій рядок: ")
line4 = input("Введіть четвертий рядок: ")

with open('file.txt', "w") as file:
    file.write(line1 + "\n")
    file.write(line2+"\n")
with open("file.txt", "a") as file:
    file.write(line3 + "\n")
    file.write(line4 + "\n")
print("Завдання виконано")
