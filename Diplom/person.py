import datetime


class Person:

    def __init__(self, first_name, last_name=None, middle_name=None, birthdate=None, deathdate=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birthdate = birthdate
        self.deathdate = deathdate
        self.gender = gender

    def calculate_age(self):
        try:
            birthdate = datetime.datetime.strptime(self.birthdate, '%d.%m.%Y').date()
            if self.deathdate:
                deathdate = datetime.datetime.strptime(self.deathdate, '%d.%m.%Y').date()
            else:
                deathdate = datetime.date.today()
            age = deathdate.year - birthdate.year - (
                        (deathdate.month, deathdate.day) < (birthdate.month, birthdate.day))
            return age
        except ValueError:
            return None

    def match_search_criteria(self, search_string):
        return search_string.lower() in self.first_name.lower() or \
               (self.last_name and search_string.lower() in self.last_name.lower()) or \
               (self.middle_name and search_string.lower() in self.middle_name.lower())

    def get_age(self):
        age = self.calculate_age()
        if age is not None:
            return age
        return "Некорректные данные о дате рождения или смерти."
