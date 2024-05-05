def print_params(param):
    print(param)
    print(param)
    return param

flag = "вход"
print("Тест-программа вывода через функцию. Для выхода введите слово "'"выход"')
while flag.lower() != "выход":
    flag = input("Введите строку:")
    print_params(flag)
print_params("Вывод функции вне основного цикла")



