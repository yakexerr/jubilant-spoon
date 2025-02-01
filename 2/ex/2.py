'''
Для последовательности из n > 1 целых чисел напечатать «ДА»,
если все числа положительные, иначе «НЕТ». Ввод чисел должен
прекращаться после введения не положительного числа.
'''
# min1 = float('inf')
n = int(input("Сколько будет чисел? "))
positive = True
for i in range(n):
    num = int(input(f"Введите {i+1} число: "))
    # if num < min1:
    #     min1 = num
    if num < 0:
        positive = False
        break
# if min1 < 0:
#     print("НЕТ")
# else:
#     print("ДА")
if positive:
    print("ДА")
else:
    print("Нет")