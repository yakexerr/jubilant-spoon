'''
13 Объединить два словаря, просуммировав значения одинаковых ключей.
Исходные данные:
{'a': 1,'b': 2,'c': 10}
{'b': 100,'e': 200}
Результат:
{'a': 1, 'b': 102, 'c': 10, 'e': 200}
может мне отдельно выписать в разные переменные ключи и значения ? проверить есть ли повторы
в ключах и если так, то просуммировать их значения и потом зип?
'''

dict1 = {'a': 1,'b': 2,'c': 10}
dict2 = {'b': 100,'e': 200}
if dict1.values() == dict2.values():
