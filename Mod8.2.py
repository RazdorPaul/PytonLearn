def personal_sum(numbers):
    sum = 0
    uncorrect = 0
    try:
        for i in numbers:
            try:
                sum += i
            except TypeError:
                uncorrect += 1
    except TypeError:
        uncorrect += 1
    return (sum, uncorrect)

def average_calc(numbers):
    average = personal_sum(numbers)
    try:
        try:
            average = average[0] / (len(numbers) - average[1])
        except ZeroDivisionError:
            average = 0
    except TypeError:
        print("Введен некорректный тип!")
        average = None
    return average

print("Сумма чисел в коллекции и количество нечисловых элементов равно ", personal_sum(('po')))
print("Среднее арифметическое чисел в коллекции равно ", average_calc(('po', 4)))
print(f'Результат 1: {average_calc("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {average_calc([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {average_calc(567)}') # Передана не коллекция
print(f'Результат 4: {average_calc([42, 15, 36, 13])}') # Всё должно работать
