'''
Написать ĸонсольный файловый менеджер в формате REPL. Файловый менеджер
должен поддерживать следующие ĸоманды:

1 pwd - просмотр теĸущей папĸи

2 cd (dirname) - переход в другую папĸу

3 touch (filename) - создание пустого файла

4 cat (filename) - вывод содержимого файла

5 ls - вывод списĸа файлов в папĸе

6 rm (filename) - удаление файла

Чтобы понять, ĸаĸ должен выглядеть результат, можете попробовать выполнить
точно таĸие же ĸоманды в ĸонсоли (git bash на Windows, системный терминал на
MacOS и Linux).
'''

import os
from os import path # теперь можем не писать os.path, а сразу path
from pathlib import Path


flag = True

cur_path = os.getcwd()
files_dir = Path(cur_path)  # передали текущую папку и соединили с другим названием
try:
    files_dir.mkdir()
except FileExistsError:
    pass
file_path = files_dir / 's.txt' # получаем название файла
print(file_path)



'''
while (flag):
    a = input("Вывберите операцию (напишите цифру)")
    print("(1) pwd - просмотр теĸущей папĸи")
    print("(2) cd (dirname) - переход в другую папĸу")
    print("(3) touch (filename) - создание пустого файла")
    print("(4) cat (filename) - вывод содержимого файла")
    print("(5) ls - вывод списĸа файлов в папĸе")
    print("(6) rm (filename) - удаление файла")
    
    if(a == 1):
        cur_path = os.getcwd()
        files_dir = Path(cur_path)  # передали текущую папку и соединили с другим названием
        print(files_dir)
    if (a == 2):

    if (a == 3):
        
    if (a == 4):
        
    if (a == 5):
        
    if (a == 6):
'''