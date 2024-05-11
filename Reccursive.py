def test(*args):
    for i in args:
        print (i)

def reccurs(num):
    if num < 1:
        return 1
    else:
        return num * reccurs(num - 1)



dict_test = {'a':1, 'b':"String", 'c': False}
list_test = [100, "Строка", (1, 2, 3)]
test(list_test)
test(dict_test)
test("Это введенная вручную строка")

while True:
    num = int(input("Введите натуральное число для вычисления факториала: "))
    print("Факториал введенного числа равен ", reccurs(num))
    num = input("Для повтора введите 1, для выхода нажмите любую клавишу: ")
    if num == '1':
        continue
    else:
        break
