from multiprocessing import Process

class UncorrectRequestException(Exception):
    def __init__(self, *args):
        if args:
            self.__message = "Запрос не может быть выполнен, такого товара на складе нет!"
        else:
            self.__message = "Запрос не может быть выполнен, товара на складе меньше, чем вы хотите отгрузить!"

    def __str__(self):
        return self.__message

class WareHouseManager():

    data = dict()

    def receipt(cls, product):
        WareHouseManager.data[product[0]] = product[1]

    def shipment(cls, product):
        if not product[0] in WareHouseManager.data:
            raise UncorrectRequestException(1)
        elif product[1] > WareHouseManager.data[product[0]]:
            raise UncorrectRequestException()
        else:
            WareHouseManager.data[product[0]] -= product[1]

    def process_request(cls, request):
        funcs = {"receipt": cls.receipt,
                 "shipment": cls.shipment}
        funcs[request[1]]((request[0], request[2]))


    def run(self, requests):
        for request in requests:
            try:
                self.process_request(request)
            except UncorrectRequestException as ex:
                print(ex)

# Создаем менеджера склада
manager = WareHouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product4", "shipment", 100),
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50),
    ("product3", "shipment", 300)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)


