import os
from  os import path # теперь можем не писать os.path, а сразу path
from  pathlib import Path
# сделаем так, чтобы открытые файлы складывались в отдельную папку
'''
cur_path = os.getcwd() # взяли путь
print(cur_path) # распечатали
# теперь получаем путь до папки, в которую сохраняем
# .path.join - внутри себя определяет, какую ОС используем ,чтобы правильно написать путь
files_dir = os.path.join(cur_path, "files") # эта функция соединяет различные части путей и мы сохраняем этот путь в переменную
print(files_dir)
# путь до папки получили, поэтому используем ф-ю mkdir - make dir - создание папки
try: # при повторном после создания выполнении кода выдаст ошибку, поэтому ловим её
    os.mkdir(files_dir)
except FileExistsError:
    pass

# собираем путь до файла
file_path = os.path.join(files_dir, 's.txt')
# получаем в созданной папке файл
# with open('s.txt', 'a+') as file:
with open(file_path, 'a+') as file:
    file.write("123")
    file.seek(0)
    print(file.read())

print(os.path.exists("s.txt"))

# также файлы можно удалять
# os.remove("s.txt")
'''

# перепишем код из комментария, кпростив при помощи pathlib

cur_path = os.getcwd()
files_dir = Path(cur_path) / "files" # передали текущую папку и соединили с другим названием
print(files_dir)
try:
    files_dir.mkdir()
except FileExistsError:
    pass
file_path = files_dir / 's.txt' # получаем название файла
with file_path.open('a+') as file:
    file.write("123")
    file.seek(0)
    print(file.read())

# проверяем сущ-ет ли файл
print(Path("s.txt").exists())



print(file_path)
print(path.basename(file_path)) # вытаскиваем название файла
print(path.dirname(file_path)) # вытаскиваем название папки
print(path.splitext(file_path)) # вытаскиваем расширение ( лучше писать название)

# при формировании путей используя ".." можем обращаться к папкам на уровень выше
print(path.join("..", "2"))
print(path.abspath(path.join("..", "2"))) # превращает путь в абсолютный

# переменные окружения (их принято нзв капсом, тк это по сути константы)
print(os.environ.get("TEST", "default value for environment variable"))