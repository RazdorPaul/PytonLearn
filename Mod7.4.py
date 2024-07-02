import os
import time

path = os.getcwd()
#path = os.path.normpath(path)
for dirpath, dirs, files in os.walk(path):
    for i in files:
        print("название файла: ", i)
        print("Полный путь к файлу: ", os.path.join(dirpath, i))
        print("Файл лежит в каталоге: ", os.path.dirname(os.path.join(dirpath, i)))
        print("Размер файла: ", os.path.getsize(os.path.join(dirpath, i)), ' bytes')
        time_ = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getatime(os.path.join(dirpath, i))))
        print("Дата последнего изменения файла: ", time_)
        print("*"  * 20)