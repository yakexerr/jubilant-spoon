'''
Вывести самое часто встречаемое число в целочисленном списке.
Если таких чисел несколько, вывести любое.
Исходные данные:
[1, 2, 3, 4, 1]
Результат:
'''
numbers = [1, 1, 1, 1, 1, 2, 3, 4, 5]
samoe_vstrech = None
maximum = 0

# перебираем "числа-кандидаты" на самые встречаемые
for kand in numbers:
    count = 0
    # считаю кол-во вхождений данного числа
    for n in numbers:
        if n == kand:
            count += 1
    # если текущая частота больше предыдущей
    if count > maximum:
        maximum = count
        samoe_vstrech = kand

print(samoe_vstrech)
