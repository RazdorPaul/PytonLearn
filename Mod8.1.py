def add_everything(a, b):
    try:
        return a + b
    except:
        return str(a) + str(b)

def is_num(a):
    try:
        a = int(a)
    except ValueError:
        try:
            a = float(a)
        except ValueError:
            pass
    return a

while True:
    a = is_num(input("Введите первое слагаемое "))
    b = is_num(input("Введите второе слагаемое "))
    print("Сумма слагаемых равна ", add_everything(a, b))
    key = input("Для выхода нажмите 'q', для повтора любую клавишу ")
    if key =='q' or key =='Q':
        break
