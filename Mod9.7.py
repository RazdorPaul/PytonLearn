def sum_tree(a, b, c):
    return a + b + c

def is_simple(func):
    def wrapper():
        summ = func
        flag = True
        for i in range(2, summ):
            if summ % i == 0:
                flag = False
                break
        return flag
    return wrapper

print("Сумма трех чисел равна", sum_tree(1, 2,4))
decor_summ = is_simple(sum_tree(1, 2, 4))
if decor_summ() == True:
    print("сумма указанных чисел простое число")
else:
    print("Сумма указанных чисел составное число")

print("Сумма трех чисел равна", sum_tree(1, 3,5))
decor_summ = is_simple(sum_tree(1, 3, 5))
if decor_summ() == True:
    print("сумма указанных чисел простое число")
else:
    print("Сумма указанных чисел составное число")