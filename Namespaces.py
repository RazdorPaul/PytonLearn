def test1():
    a = 5
    b = "Это тестовая функция"
    print("Первая локальная переменная:", a)
    print("Вторая локальная переменная:", b)


def test2(a, b, c):
    print("Первый параметр:", a)
    print("Второй параметр:", b)
    print("Третий параметр:", c)


test1()
test2("Это переданная строка", 100, False)