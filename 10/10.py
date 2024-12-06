'''
Есть два словаря. Необходимо объединить их и сохранить в третий.
Исходные данные:
{'a': 1,'b': 2,'c': 10}
{'b': 100,'e': 200}
Результат:
{'a': 1, 'b': 100, 'c': 10, 'e': 200}
'''

dict1 = {'a': 1,'b': 2,'c': 10}
dict2 = {'b': 100,'e': 200}
dict3 = dict1.copy()
dict3.update(dict2)

print(dict3)

