from data_manager import DataManager


def main():
    data_manager = DataManager()

    while True:
        print("1. Добавить новую запись")
        print("2. Искать запись")
        print("3. Выйти")
        choice = input("Выберите опцию: ")

        if choice == "1":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию (или нажмите Enter): ")
            middle_name = input("Введите отчество (или нажмите Enter): ")
            birthdate = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
            deathdate = input("Введите дату смерти (в формате ДД.ММ.ГГГГ или нажмите Enter): ")
            gender = input("Введите пол: ")

            data_manager.add_person(first_name, last_name, middle_name, birthdate, deathdate, gender)
            print("Запись добавлена успешно!")

        elif choice == "2":
            search_string = input("Введите строку для поиска: ")
            results = data_manager.search_people(search_string)
            if results:
                print("\n".join(results))
            else:
                print("Запись не найдена.")
        elif choice == "3":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите существующую опцию.")


if __name__ == "__main__":
    main()
