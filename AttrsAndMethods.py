class House:
    def __init__(self, name_, floors_):
        self.name = name_
        self.floors = floors_

    def go_to(self, floor):
        if floor > self.floors:
            print(f"Этажа {floor} нет в этом здании")
        else:
            for i in range(1, floor + 1):
                print("вы на этаже ", i, " В доме", self.name)

house1 = House("ЖК Солнечный", 20)
house2 = House("ДНТ Усадьба", 5)
house1.go_to(10)
house1.go_to(30)
house2.go_to(4)
house2.go_to(6)