class Auto:
    def __init__(self, brand, age, mark, color="", weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print(f"{self.brand} Move")

    def stop(self):
        print(f"{self.brand} Stop")

    def birthday(self):
        self.age += 1
