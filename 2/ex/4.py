'''
Для последовательности из n > 1 целых чисел напечатать «ДА»,
если числа образуют арифметическую прогрессию в порядке их
следования и «НЕТ» в противном случае. В первой строке задаётся
количество чисел в последовательности, а во второй - сами числа.
Исходные данные:
5
-1 1 3 5 7
Результат:
ДА
'''

n = int(input("Сколько всего? "))
prev = None
vozrastaet = True
for i in range(n):
    num = int(input(f"Введите {i+1} число: "))
    if prev is not None:
        if num != prev + 2:
            vozrastaet = False
        else:
            vozrastaet = True
    prev = num
if vozrastaet:
    print("ДА")
else:
    print("НЕТ")