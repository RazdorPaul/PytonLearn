class Vehicle:
    __COLORS = ["BLACK", "WHITE", "RED", "SNOW_QWEEN", "BLUE", "GRAY"]

    def __init__(self, name, model, power, color):
        self.__owner = name
        self.__model = model
        self.__engine_power = power
        self.__color = color

    def getOwner(self):
        return self.__owner

    def getModel(self):
        return self.__model

    def getPower(self):
        return self.__engine_power

    def getColor(self):
        return self.__color

    def setColor(self, color: str):
        if color.upper() in self.__COLORS:
            self.__color = color.upper()
        else:
            print(f"Ваш авто цвета {self.getColor()} нельзя перекрасить в цвет {color}")

    def setOwner(self, name):
        self.__owner = name
        print(f"Новый владелец авто {self.__owner}")

    def print_info(self):
        print(f"Марка, модель:{self.getModel()}\n"
              f"Мощность двигателя в л.с.: {self.getPower()}\n"
              f"Цвет авто: {self.getColor()}\n"
              f"Владелец авто: {self.getOwner()}")


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


car = Sedan("Рыжаков Ю.С", "Toyota Mark X", 215, "SNOW_QWEEN")
car.print_info()
car.setColor("pink")
car.setColor("black")
car.setOwner("Раздорожный П.В")
car.print_info()