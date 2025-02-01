numbers = [1,2,3]
# print(sum([n**2 for n in numbers])) # сумма квадратов
print(sum([n for n in numbers if n % 2 == 1])) # сумма нечётных
print(sum([1 for n in numbers if n % 2 == 1])) # кол-во нечётных

# all - возвращает True если все эл-ты True
numbers1 = [1, 3, 5]
print(all([n % 2 == 1 for n in numbers1]))#проверка, что все числа нечётные
if numbers1 != []:
    print(all([n % 2 == 1 for n in numbers1])) #Прошлое ТЗ + если список пустой ⇒ false

sequence = [1, -2, 3]
print(all([bool(x) for x in sequence]))

# any - есть ли хотябы один True