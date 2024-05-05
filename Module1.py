scores = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Подсчитаем средние оценки в списке оценок
for i in range(len(scores)):
    scores[i] = sum(scores[i]) / len(scores[i])

# Конвертируем множество студентов в список и сортируем
students = sorted(students)

# Создаем словарь и заполняем парами "Имя":"средний балл"
average_scores = {}
for i in range(len(students)):
    average_scores[students[i]] = scores[i]

# Выводим словарь с оценками
print(average_scores)