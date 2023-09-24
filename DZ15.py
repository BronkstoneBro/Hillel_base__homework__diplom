def finish(input_str):
    if input_str.lower() in ["вихід", "exit", "quit", "e", "q"]:
        return "exit"

    if input_str.startswith('--'):
        return f"Ви ввели неправильне число: {input_str}"

    if input_str.startswith('-') and input_str[1:].isdigit():
        number = int(input_str)
        return f"Ви ввели від'ємне ціле число: {number}"

    elif input_str.isdigit():
        number = int(input_str)
        if number == 0:
            return "Ви ввели нуль"
        elif number > 0:
            return f"Ви ввели позитивне ціле число: {number}"
        else:
            return f"Ви ввели від'ємне ціле число: {number}"
    else:
        try:
            number = float(input_str.replace(",", "."))
            if number < 0:
                return f"Ви ввели від'ємне дробове число:  {number}"
            elif number > 0:
                return f"Ви ввели позитивне дробове число: {number}"
            else:
                return "Ви ввели нуль"
        except ValueError:
            return f"Ви ввели неправильне число: {input_str}"


while True:
    user_input = input("Введіть будь яке число, або 'вихід', "
                       "'exit', 'quit', 'e', 'q' для виходу: ")
    result = finish(user_input)
    if result == "exit":
        break
    print(result)
