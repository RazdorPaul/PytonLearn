from random import choice

class MysticBall:
    def __init__(self, *strings):
        self.words = strings

    def __call__(self):
        return choice(self.words)

def get_advanced_writer(file_name):
    def write_everything(*args):
        with open(file_name, 'a', encoding="utf-8") as my_file:
            for i in args:
                print(f"{i}\n", file=my_file)
    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first = MysticBall("Да", "Нет", "Наверное", "Может быть", "Не знаю")
print(first())
print(first())
print(first())
print(first())