import time


class Auto:
    def __init__(self, brand, age, mark, color="", weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):

        super().move()
        print(f"Max speed is {self.max_speed}")


truck_1 = Truck("Mercedes", 2018, "Actros", 10000, "White", 8000)
truck_2 = Truck("Volvo", 2020, "FM", 35000, "Black", 15000)

car_1 = Car("Lamborghini", 2022, "Aventador", 350, "White", 1500)
сar_2 = Car("Rolls Royce", 2020, "Phantom", 250, "Black", 2500)

print(f'Name of the first Truck brand: {truck_1.brand}')
print(f'Name of the first Truck age: {truck_1.age}')
print(f'Name of the first Truck color: {truck_1.color}')
print(f'Name of the first Truck mark: {truck_1.mark}')
print(f'Name of the first Truck weight: {truck_1.weight}')
print(f'Name of the first Truck max load: {truck_1.max_load}')
truck_1.move()
truck_1.stop()
truck_1.birthday()
print(f'Age of first Truck: {truck_1.age}')
truck_1.load()

print(f'Name of the second Truck brand: {truck_2.brand}')
print(f'Name of the second Truck age: {truck_2.age}')
print(f'Name of the second Truck color: {truck_2.color}')
print(f'Name of the second Truck mark: {truck_2.mark}')
print(f'Name of the second Truck weight: {truck_2.weight}')
print(f'Name of the second Truck max load: {truck_2.max_load}')
truck_2.move()
truck_2.stop()
truck_2.birthday()
print(f'Age of the second Truck: {truck_2.age}')
truck_2.load()

print(f'Name of first Car brand: {car_1.brand}')
print(f'Name of first Car age: {car_1.age}')
print(f'Name of first Car color: {car_1.color}')
print(f'Name of first Car mark: {car_1.mark}')
print(f'Name of first Car weight: {car_1.weight}')
print(f'Name of first Car max speed: {car_1.max_speed}')
car_1.move()
car_1.birthday()
print(f'Age of first Car: {car_1.age}')
car_1.stop()

print(f'Name of the second Car brand: {сar_2.brand}')
print(f'Name of the second Car age: {сar_2.age}')
print(f'Name of the second Car color: {сar_2.color}')
print(f'Name of the second Car mark: {сar_2.mark}')
print(f'Name of the second Car weight: {сar_2.weight}')
print(f'Name of the second Car max speed: {сar_2.max_speed}')
сar_2.move()
сar_2.birthday()
print(f'Age of the second Car: {сar_2.age}')
сar_2.stop()
