def add_everything(a, b):
    try:
        return a + b
    except:
        return str(a) + str(b)

while True:
    a = input("Введите первое слагаемое ")
    b = input("Введите второе слагаемое ")
    if a.isnumeric():
        a = int(a)
    if b.isnumeric():
        b = int(b)
    print("Сумма слагаемых равна ", add_everything(a, b))
    key = input("Для выхода нажмите 'q', для повтора любую клавишу ")
    if key =='q' or key =='Q':
        break
