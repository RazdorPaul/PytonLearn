
#Задача 1. Определение вида треугольника
def input_triangle():
    a = int(input("Введите сторону 1: "))
    b = int(input("Введите сторону 2: "))
    c = int(input("Введите сторону 3: "))
    return a, b, c


print("\nОпределение вида треугольника")
while True:
    a, b, c = input_triangle()
    if a == b and a == c:
        print("Ваш треугольник равносторонний!")
    elif a == b or a == c or b == c:
        print("Ваш треугольник равнобедренный!")
    else:
        print("Ваш треугольник разносторонний!")
    buff = input("Для повтора нажмите 1, для продолжения Enter ")
    if buff == '1':
        continue
    else:
        break


# Задача на определение среднего числа
def input_num():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    return a, b, c


print("\nОпределение среднего числа")
while True:
    a, b, c =  input_num()
    if a < b < c or a > b > c:
        print("Среднее число из трех равно ", b)
    elif c < a < b or c > a > b:
        print("Среднее число из трех равно ", a)
    elif a < c < b or a > c > b:
        print("Среднее число из трех равно ", c)
    else :
        print("Среднего нет, два или три числа равны ")
    buff = input("Для повтора нажмите 1, для продолжения Enter ")
    if buff == '1':
        continue
    else:
        break


# Задача на определение цвета
def input_color():
    while True:
        str_colors = input("Введите два цвета- красный, желтый или синий: ").lower()
        list_colors = str_colors.replace(',', '').split()
        for i in reversed(list_colors):
            if i != "красный" and i !=  "желтый" and i != "синий":
                list_colors.remove(i)
        if len(list_colors) != 2:
            print("Вы указали неправильные цвета, повторите ввод")
        else:
            break
    return list_colors[0], list_colors[1]


print("\nОпределение цвета")
while True:
    color1, color2 = input_color()
    if (color1 == "красный" and color2 =="желтый") or (color2 == "красный" and color1 =="желтый"):
        print("При смешивании этих цветов получится оранжевый цвет")
    elif (color1 == "красный" and color2 =="синий") or (color2 == "красный" and color1 =="синий"):
        print("При смешивании этих цветов получится фиолетовый цвет")
    elif (color1 == "синий" and color2 =="желтый") or (color2 == "синий" and color1 =="желтый"):
        print("При смешивании этих цветов получится зеленый цвет")
    else:
        print("Указанные цвета одинаковы, цвет не изменится!")
    buff = input("Для повтора нажмите 1, для продолжения Enter ")
    if buff == '1':
        continue
    else:
        break


#Вывод треугольника из звездочек
def input_height():
    while True:
        num = int(input("Введите натуральное число от 1 до 80: ")) #ограничим ввод до стандартной ширины консоли
        if num < 1 or num > 80:
            print("Введенное значение не соответствует диапазону, повторите!")
        else:
            break
    return num


print("\nВывод треугольника из звездочек")
while True:
    height = input_height()
    for i in range(1, height + 1):
        print('*' * (height - i + 1))
    buff = input("Для повтора нажмите 1, для продолжения Enter ")
    if buff == '1':
        continue
    else:
        break


#Фрагмент таблицы умножения
def input_ranges():
    while True:
        flag_is_numeric = True
        ranges = input("Введите 4 числа в диапазоне от 1 до 10: ").split()
        if len(ranges) != 4:
            print("Некорректный ввод, повторите!")
            continue
        for i in range(4):
            ranges[i] = ranges[i].replace(',', '')
            ranges[i] = ranges[i].replace('.', '')
            if ranges[i].isnumeric() == False:
                flag_is_numeric = False
                break
            ranges[i] = int(ranges[i])
            if ranges[i] > 10 or ranges[i] < 1:
                flag_is_numeric = False
                break
        if flag_is_numeric == False:
            print("Некорректный ввод, повторите!")
            continue
        else:
            break
    if ranges[0] > ranges[1]:
        ranges[0] += ranges[1]
        ranges[1] = ranges[0] - ranges[1]
        ranges[0] = ranges[0] - ranges[1]
    if ranges[2] > ranges[3]:
        ranges[2] += ranges[3]
        ranges[3] = ranges[2] - ranges[3]
        ranges[2] = ranges[2] - ranges[3]
    return ranges[0], ranges[1], ranges[2], ranges[3],


print("\nВывод таблицы умножения")
while True:
    left1, right1, left2, right2 = input_ranges()
    temp_str ='\t'
    for i in range(left2 , right2 + 1):
        temp_str = temp_str + str(i) + '\t'
    print(temp_str)
    for i in range(left1 , right1 + 1):
        temp_str = str(i) + '\t'
        for j in range(left2, right2+1):
            temp_str = temp_str + str(i*j) + '\t'
        print(temp_str)
    buff = input("Для повтора нажмите 1, для продолжения Enter ")
    if buff == '1':
        continue
    else:
        break


#Вывод численного треугольника
def input_num():
    while True:
        num = int(input("Введите натуральное число от 1 до 80: "))
        if num < 1 or num > 80:
            print("Некорректный ввод, повторите!")
            continue
        else:
            break
    return num


print("\nВывод треугольника из чисел")
while True:
    num_height = input_num()
    temp_num = 1
    for i in range(1, num_height + 1):
        temp_str = ''
        for j in range(1, i + 1):
            temp_str = temp_str + ' ' + str(temp_num)
            temp_num = temp_num + 1
        print(temp_str)
    buff = input("Для повтора нажмите 1, для продолжения Enter ")
    if buff == '1':
        continue
    else:
        break