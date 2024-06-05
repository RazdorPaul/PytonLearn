class Building:

    name = ""

    def __init__(self, floors: int, type_: str):
        self.numberOfFloors = floors
        self.buildingType = type_

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors
                and self.buildingType == other.buildingType)


house1 = Building(int(input("укажите этажность ")),
                  input("укажите тип здания "))
house1.name = input("укажите имя здания ")
house2 = Building(int(input("укажите этажность ")),
                  input("укажите тип здания "))
house2.name = input("укажите имя здания ")
if house1 == house2:
    print(f"здание {house1.name} равно зданию {house2.name}")
else:
    print(f"здание {house1.name}  не равно зданию {house2.name}")