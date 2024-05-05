print("Вас приветствует программа подбора паролей")
print("Для выхода введите 0")
pass_key = 1
password = []

while pass_key != 0:
    pass_key = int(input("Введите число от 3 до 20: "))
    # Проверка пользовательсого ввода
    if pass_key == 0:
        break
    if pass_key < 3 or pass_key > 20:
        print("Число НЕ соответствует диапазону!!!")
        continue

    # Составим список из делителей введенного числа
    divisors = []
    for i in range(3, pass_key + 1):
        if (pass_key % i) == 0:
            divisors.append(i)

    # Подберем уникальные пары для каждого делителя
    for i in range(1, pass_key):
        for j in range(len(divisors)):
            if i < (divisors[j] - i):
                password.append(i)
                password.append(divisors[j]-i)

    # Преобразуем список в итоговый результат
    result=""
    for i in range(len(password)):
        result += str(password[i])

    # Обнулим список перед следующей итерацией
    password = []

    # Выведем результат
    print(result)