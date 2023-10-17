import tkinter as tk
from tkinter import messagebox
from data_manager import DataManager


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager()

        self.title("Дипломная работа")
        self.geometry("500x500")

        self.label = tk.Label(self, text="Выберите опцию:")
        self.label.pack()

        self.button_add = tk.Button(self, text="Добавить новую запись", command=self.show_add_window)
        self.button_add.pack()

        self.button_search = tk.Button(self, text="Искать запись", command=self.show_search_window)
        self.button_search.pack()

        self.button_exit = tk.Button(self, text="Выйти", command=self.destroy)
        self.button_exit.pack()

    def show_add_window(self):
        add_window = AddWindow(self)

    def show_search_window(self):
        search_window = SearchWindow(self)


class AddWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Добавить новую запись")

        self.label_first_name = tk.Label(self, text="Имя:")
        self.label_first_name.pack()
        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.pack()

        self.label_last_name = tk.Label(self, text="Фамилия:")
        self.label_last_name.pack()
        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.pack()

        self.label_middle_name = tk.Label(self, text="Отчество:")
        self.label_middle_name.pack()
        self.entry_middle_name = tk.Entry(self)
        self.entry_middle_name.pack()

        self.label_birthdate = tk.Label(self, text="Дата рождения (ДД.ММ.ГГГГ):")
        self.label_birthdate.pack()
        self.entry_birthdate = tk.Entry(self)
        self.entry_birthdate.pack()

        self.label_deathdate = tk.Label(self, text="Дата смерти (ДД.ММ.ГГГГ или нажмите Enter):")
        self.label_deathdate.pack()
        self.entry_deathdate = tk.Entry(self)
        self.entry_deathdate.pack()

        self.label_gender = tk.Label(self, text="Пол:")
        self.label_gender.pack()
        self.entry_gender = tk.Entry(self)
        self.entry_gender.pack()

        self.button_add = tk.Button(self, text="Добавить", command=self.add_record)
        self.button_add.pack()

    def add_record(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        middle_name = self.entry_middle_name.get()
        birthdate = self.entry_birthdate.get()
        deathdate = self.entry_deathdate.get()
        gender = self.entry_gender.get()

        if not self.master.data_manager.validate_date(birthdate) or (
                deathdate and not self.master.data_manager.validate_date(deathdate)):
            messagebox.showerror("Ошибка", "Некорректная дата. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.")
        else:
            self.master.data_manager.add_person(first_name, last_name, middle_name, birthdate, deathdate, gender)
            age = self.master.data_manager.search_people(first_name)[
                -1]  # Получаем возраст из последней найденной записи
            messagebox.showinfo("Успех", f"Запись добавлена успешно! {middle_name}, {age}")
            self.destroy()


class SearchWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Искать запись")

        self.label_search = tk.Label(self, text="Введите строку для поиска:")
        self.label_search.pack()

        self.entry_search = tk.Entry(self)
        self.entry_search.pack()

        self.button_search = tk.Button(self, text="Поиск", command=self.search_records)
        self.button_search.pack()

        self.results_label = tk.Label(self, text="")
        self.results_label.pack()

    def search_records(self):
        search_string = self.entry_search.get()
        results = self.master.data_manager.search_people(search_string)
        if results:
            self.results_label.config(text="\n".join(results))
        else:
            self.results_label.config(text="Запись не найдена.")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
