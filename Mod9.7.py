def is_simple(func):
    def wrapper(*args):
        summ = func(*args)
        print(f"Сумма чисел равна {summ}")
        flag = True
        for i in range(2, summ):
            if summ % i == 0:
                flag = False
                break
        if flag:
            print(f"Сумма чисел простое число")
        else:
            print(f"Сумма чисел составное число")
    return wrapper

@is_simple
def sum_tree(a, b, c):
    return a + b + c


is_simple(sum_tree(1,2,4))
is_simple(sum_tree(1,3,4))
is_simple(sum_tree(1,4,6))