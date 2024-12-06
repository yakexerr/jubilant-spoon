'''
Рассматриваются все числа от 1 до n. Сколько раз встречается
каждая цифра от 0 до 9 во всех этих числах вместе взятых? Для
каждой цифры вывести ее и количество вхождений.
Исходные данные:
n = 17
Результат вывода в консоль:
0:1, 1:10, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:1, 9:1
'''
n = 17


s = ''.join(str(i) for i in range(1, n + 1))


d = {}


# первый способ
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

# Формируем строку вывода
result = ', '.join([f"{k}:{v}" for k, v in d.items()])
print(result)

# второй способ
for i, (k,v) in enumerate(d.items()):
    end = '\n' if i == len(d) - 1 else ', '
    print(f'{k}:{v}', end = end)


# третий способ (без индексов)
array = '1 2 3'
is_first = True # флаг - является ли первой итерацие
for a in array:
    before = '' if is_first else ", "
    print(before, a, sep='', end = '')
    is_first = False
print()


# удобная фича
# a = 1
# print(f"{a=}")