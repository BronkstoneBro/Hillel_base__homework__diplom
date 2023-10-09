class NegativeExponentErrors(Exception):
    pass


class Calculator:
    def add(self, x, y):
        try:
            return x + y
        except Exception as e:
            return f"Помилка: {e}"

    def subtract(self, x, y):
        try:
            return x - y
        except Exception as e:
            return f"Помилка: {e}"

    def multiply(self, x, y):
        try:
            return x * y
        except Exception as e:
            return f"Помилка: {e}"

    def divide(self, x, y):
        try:
            if y == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе")
            return x / y
        except ZeroDivisionError as e:
            return f"Помилка {e}"
        except Exception as e:
            return f"Помилка {e}"

    def power(self, x, y):
        try:
            if y < 0:
                raise NegativeExponentErrors("Піднесення до "
                                             "негативного ступеня неможливе")
            return x ** y
        except NegativeExponentErrors as e:
            return f"Помилка: {e}"
        except Exception as e:
            return f"Помилка: {e}"

    def square_root(self, x):
        try:
            if x < 0:
                raise ValueError("Корінь від від'ємного числа неможливий")
            return x ** 0.5
        except ValueError as e:
            return f"Помилка: {e}"
        except Exception as e:
            return f"Помилка: {e}"


calc = Calculator()
print(calc.add(5, 5))
print(calc.subtract(20, 5))
print(calc.multiply(5, 3))
print(calc.divide(8, 2))
print(calc.divide(6, 0))
print(calc.power(2, 3))
print(calc.power(2, -3))
print(calc.square_root(25))
print(calc.square_root(-25))
