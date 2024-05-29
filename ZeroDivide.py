import FakeDivide as fake
import TrueDivide as truth

print("Вы в программе деления двух чисел")
while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат деления по правилам школьной арифметики равен ", fake.ZeroDivide(a, b))
    print("Результат деления по правилам высшей математики равен ", truth.ZeroDivide(a, b))
    if input("Для повтора введите 0, для выхода любую клавишу ") != '0':
        break