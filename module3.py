def size_of_struct(data_struct, sum_num, len_str):
    for i in data_struct:
        if type(i) == int or type(i) == float:
            sum_num += i
        elif type(i) == str:
            len_str += len(i)
        elif type(i) == dict:
            sum_num, len_str = size_of_struct(i.items(), sum_num, len_str)
        else:
            sum_num, len_str = size_of_struct(i, sum_num, len_str)
    return sum_num, len_str


def input_value():
    value_ = []
    key_ = 10
    while value_ != 0:
        print("Вводим число, структуру или строку?:")
        key_ = input("\tВведите 1 для ввода числа\n"
                     "\tВведите 2 для ввода строки\n"
                     "\tВведите 3 для ввода структуры\n"
                     "\tВведите 4 для конца ввода\n")
        if key_ == '1':
            value_.append(int(input("Введите число ")))
        elif key_ == '2':
            value_.append(input("Введите строку "))
        elif key_ == '3':
            value_.append(input_struct())
        elif key_ == '4':
            break
        else:
            print("Непонятно, повторите")
            continue
    return value_


def input_dict():
    data_ = dict()
    while True:
        key_ = input("Введите ключ. Ввод символа ! закончит заполнение словаря: ")
        if key_ == '!':
            break
        if key_.isnumeric():
            key_ = int(key_)
        print("Введите значение ключа: \n")
        value_ = input_value()
        if len(value_) == 1:
            value_ = value_[0]
        data_.update({key_: value_})
    return data_



def input_struct():
    data_ = []
    key_ = 0
    while key_ != '6':
        print("Что добавляем?")
        key_ = input("\tВведите 1 для выбора кортежа\n"
                     "\tВведите 2 для выбора множества\n"
                     "\tВведите 3 для выбора списка\n"
                     "\tВведите 4 для выбора словаря\n"
                     "\tВведите 5 для ввода элементов\n"
                     "\tВведите 6 для конца ввода\n")
        if key_ == '1':
            data_ = tuple(input_value())
        if key_ == '2':
            data_ = set(input_value())
        if key_ == '3' or key_ == '5':
            data_ = input_value()
        if key_ == '4':
            data_ = input_dict()
    print("Вывод введенной структуры\n", data_)
    return data_


# Тело основной программы.
print("Вы в программе определения размера ползовательской структуры данных")
print("Под размером понимается длинна всех строчных данных")
print("И сумма всех численных данных в этой структуре.")
while True:
    print("Желаете ли вы посмотреть пример или ввести структуру вручную?")
    input_mode = input("1-Посмотреть пример/2-ручной ввод ")
    if input_mode != '1' and input_mode != '2':
        print("Не очень понятно, чего вы хотите, повторите ввод\n")
        continue
    data_struct = [[1, 2, 3],
                   {'a': 4, 'b': 5},
                   (6, {'cube': 7, 'drum': 8}),
                   "Hello",
                   ((), [{(2, 'Urban', ('Urban2', 35))}])
                   ]
    if input_mode == '1':
        print("Вывод структуры-примера\n", data_struct)
    if input_mode == '2':
        print("При выборе элемента будет создан список!")
        data_struct = input_struct()
    sum_data, len_data = size_of_struct(data_struct, 0, 0)
    print("Сумма численных элементов структуры равно ", sum_data)
    print("Сумма длин всех строк структуры равна ", len_data)
    print("Общий размер структуры равен ", sum_data+len_data)
    if input("Для повтора введите 1, для выхода любую клавишу ") != '1':
        break
