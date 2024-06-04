class House:
    def __init__(self, name_):
        self.name = name_
        self.num_floors = 0

    def setNumberOfFloor(self, num):
        self.num_floors = num

house = House(input("Укажите название здания "))
print("Начальное количество этажей ", house.num_floors)
house.setNumberOfFloor(int(input("Введите желаемое количество этажей ")))
print(f"Высота здания {house.name} равна ", house.num_floors)