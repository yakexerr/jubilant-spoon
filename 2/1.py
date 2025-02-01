'''
Вводится n - сколько чисел
Потом сами числа
вывести максимум
'''
max = float("-inf")
n = int(input("Сколько чисел: "))

i =0
while i < n:
    num = int(input("Введите число: "))
    if num > max:
        max = num
    i+=1
print(max)