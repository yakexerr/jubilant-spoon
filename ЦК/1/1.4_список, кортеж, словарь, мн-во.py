lst = [1,2,3]

lst.append(4) # добавление элемента
print(lst)
print(lst[0])
lst.remove(3) # удаление элемента
print(lst)
if 2 in lst:
    print("2 есть в списке")
else:
    print("2 нет в списке")


#lst_console = input("Введите список чисел через пробел: ")
#numbers = lst_console.split(" ")
#print(numbers)

# картежи - вводится 1 раз и изменить его нельзя
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

print("___________-------------__________")

# tuple и списки можно распаковывать в несколько переменных
first, second, third = tup
print("1",first)
print("2",second)
print("3",third)

print(3 in tup) # проверка наличия элемента

# СЛОВАРЬ - объявляется при помощи фигурных скобок, слеваа ключ справа значение (ключ:значение)

eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

print(eng_rus_dict)
print(eng_rus_dict['cat'])
#по ключу можно не только выводить значения ,но и записывать
eng_rus_dict['cat'] = 'Кошка'
print(eng_rus_dict['cat'])

#проверка наличия
print("car" in eng_rus_dict)
print(eng_rus_dict.values()) # выводи значения словаря
print("кот" in eng_rus_dict.values())
print(eng_rus_dict.keys()) # вывод ключей словаря
print(eng_rus_dict.items()) # возвращает пары ключ-значение

# получение значения из словаря (вторым значением передаём то, что будет выведене при отсутствии значения (если не укажем выведет None))
print(eng_rus_dict.get("brother", "(нет перевода)"))


print("________________------------------_______________")

# Множества - можно создать на базе списка

set_from_list = set(lst)
set_example = {1, 2, 3}
print(set_example)
print(set_from_list)

set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example - {3, 5})
# объединение множеств
print(set_example.union({6,7}))
# сравнение (!!!!! ВАЖНО - в мн-ве не важен порядокБ поэтому множества 1,2,3 и 3,1,2 равны
print(set_example == {1, 5, 3})

print(len("брат"))
print(len(lst))
print(len(eng_rus_dict))
print(len(set_example))