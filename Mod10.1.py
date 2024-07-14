from time import sleep
from datetime import datetime
from threading import Thread

def write_words(count, namefile):
    with open(namefile, 'w', encoding="utf-8") as file:
        for i in range(count):
            print(f"Какое-то слово № {i + 1}", file=file)
            sleep(0.1)
        print(f"Завершилась запись в файл {namefile}")

start_time = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = datetime.now()
print(f"Время записи составляет {end_time - start_time}")

start_time = datetime.now()
first = Thread(target=write_words, args=(10, "example5.txt",))
first.start()
second = Thread(target=write_words, args=(30, "example6.txt",))
second.start()
third = Thread(target=write_words, args=(200, "example7.txt",))
third.start()
fourth = Thread(target=write_words, args=(100, "example8.txt",))
fourth.start()

first.join()
second.join()
third.join()
fourth.join()
end_time = datetime.now()
print(f"Время записи составляет {end_time - start_time}")