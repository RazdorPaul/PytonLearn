def print_params(a=1, b="строка", c=True):
    print("Первый параметр:", a)
    print("Второй параметр:", b)
    print("Третий параметр:", c, "\n")


print_params()
print_params(10)
print_params(100, "100")
print_params(False, False, False)

list_ = [50, "QWERTY", True]
list_2 = [1000, "тысяча"]
dict_ = {'a':100, 'b':"ЙЦУКЕН", 'c':True}

print_params(*list_)
print_params(**dict_)
print_params(*list_2)
print_params(*list_2, False)
