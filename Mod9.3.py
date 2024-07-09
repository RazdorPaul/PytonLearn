first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zp = zip(first,second)
first_result = (len(x[0]) -len(x[1]) if
                len(x[0]) > len(x[1]) else
                len(x[1]) - len(x[0]) for x in zp if len(x[0]) != len(x[1]))

print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(second_result))