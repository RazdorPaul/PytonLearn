from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        self.__name = name
        self.__power = power
        self.__enemy =100
        super().__init__()

    def run(self):
        print(f"Сэр {self.__name}, на нас напали!")
        time_of_battle = 0
        while(self.__enemy > 0):
            sleep(1)
            time_of_battle += 1
            self.__enemy -= self.__power
            print(f"Рыцарь {self.__name} сражается {time_of_battle} день(дня), осталось сразить {self.__enemy} воинов")
        print(f"Сэр {self.__name} одержал победу спустя {time_of_battle}")

first = Knight("Ланселот", 10)
second = Knight("Галахад", 20)
first.start()
second.start()
first.join()
second.join()
print("Все враги побеждены!")
