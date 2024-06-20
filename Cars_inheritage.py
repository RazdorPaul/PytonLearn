class Car:
    def __init__(self):
        self.price = 1000000

    def getPower(self):
        return 1000

class Vehicle:
    def __init__(self):
        self.vehicle_type = None

class Nissan(Car, Vehicle):
    def __init__(self):
        self.price = 500000
        self.vehicle_type = "sedan"

    def getPower(self):
        return 120


car = Nissan()
print(f"Тип кузова: {car.vehicle_type}")
print(f"Стоимость авто: {car.price}")
print(f"Мощность двигателя: {car.getPower()}")