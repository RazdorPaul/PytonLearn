class UncorrectVinNumber(Exception):
    def __init__(self, vin):
        self.min = 1000000
        self.max = 9999999
        self.vin = vin

    def __str__(self):
        return (f"Значение {self.vin} не входит в допустимый диапазон!\n"
                f"Vin должен быть в диапазоне от {self.min} до {self.max}!")

class UncorrectCarNumber(Exception):
    def __str__(self):
        return (f"Некорректно указан номер!\n"
                f"Номер должен быть сттрокой и состоять из 6 знаков!")

class Car:
    def __init__(self, model, vin, number):
        self.__model = model
        if self.__isValidVin(vin):
            self.__vin = vin
        else:
            self.__vin = None
            raise UncorrectVinNumber(vin)
        if self.__isValidNumber(number):
            self.__number = number
        else:
            self.__number = None
            raise UncorrectCarNumber()

    def __isValidVin(self, vin):
        if isinstance(vin, int) and 1000000 <= vin <= 9999999:
            return True

    def __isValidNumber(self, number):
        if isinstance(number, str) and len(number) == 6:
            return True

    def getVin(self):
        return self.__vin

    def geNumber(self):
        return self.__number

    def getModel(self):
        return self.__model


try:
  first = Car('Model1', 1000000, 'f123dj')
  print(f'{first.getModel()} успешно создан')
except UncorrectVinNumber as exc:
  print(exc)
except UncorrectCarNumber as exc:
  print(exc)

try:
  second = Car('Model2', 300, 'т001тр')
  print(f'{second.getModel()} успешно создан')
except UncorrectVinNumber as exc:
  print(exc)
except UncorrectCarNumber as exc:
  print(exc)

try:
  third = Car('Model3', 2020202, 4568)
  print(f'{third.getModel()} успешно создан')
except UncorrectVinNumber as exc:
  print(exc)
except UncorrectCarNumber as exc:
  print(exc)