from threading import Thread
from queue import Queue
from time import sleep

class Cafe:
    def __init__(self, *tables):
        self.__tables = list(tables)
        self.que = Queue()

    def customer_arrival(self):
        num = 1
        while num <= 40:
            print(f"Посетитель {num} прибыл")
            self.customer_service(Customer(num, self))
            num += 1
            sleep(1)


    def customer_service(self, customer):
        table = None
        for table_ in self.__tables:
            if not table_.is_bisy:
                table = table_
                break
        if table != None:
            customer.customer_table = table
            customer.start()
        else:
            print(f"Посетитель {customer.number} ожидает свободный столик")
            self.que.put(customer)

class Table:
    def __init__(self, num: int):
        self.__number = num
        self.__is_bisy = False

    @property
    def number(self):
        return self.__number

    @property
    def is_bisy(self):
        return self.__is_bisy

    @is_bisy.setter
    def is_bisy(self, flag):
        self.__is_bisy = flag

class Customer(Thread):
    def __init__(self, num_pers, cafe):
        super().__init__()
        self.__num = num_pers
        self.__table = None

    def run(self):
        print(f"Посетитель {self.__num} сел за столик {self.__table.number}")
        self.__table.is_bisy = True
        sleep(5)
        self.__table.is_bisy = False
        print(f"Посетитель {self.__num} покушал и ушел")
        if not cafe.que.empty():
            cafe.customer_service(cafe.que.get())

    @property
    def customer_table(self):
        return self.__table

    @customer_table.setter
    def customer_table(self, num_table):
        self.__table = num_table

    @property
    def number(self):
        return self.__num

cafe = Cafe(Table(1), Table(2), Table(3), Table(4))
thread_ = Thread(target=cafe.customer_arrival)
thread_.start()
thread_.join()