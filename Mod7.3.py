team1 = "Волшебники данных"
team2 = "Мастера кода"
team1_num = 5
team2_num = 5
score1 =40
score2 =42
team1_time = 1552.51
team2_time = 2153.31
task_total =score1 + score2
time_avg = (team1_time + team2_time) / task_total
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    result = f"Победила команда {team1}"
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    result = f"Победила команда {team2}"
else:
    result = "Ничья"

print("В команде %s учавствует %d человек"%(team1, team1_num))
print("В команде %s учавствует %d человек"%(team2, team2_num))
print("Итого в командах сегодня %s и %d человек!\n"%(team1_num, team2_num))
print("Команда {0} решила {1} задач за {2} секунд".format(team1, score1, team1_time))
print("Команда {0} решила {1} задач за {2} секунд\n".format(team2, score2, team2_time))
print(f"Итог сегодняшнего соревнования: {result}\n")
print(f"В соревновании было решено {task_total} задач")
print(f"Среднее время решения одной задачи составило {time_avg:.2f} секунд")