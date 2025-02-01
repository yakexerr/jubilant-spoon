'''
Вывести самый часто встречаемый символ в строке без учёта ре-
гистра. Если таких символов несколько, вывести любое.
Исходные данные:
HeLlo
Результат:
L # или l
'''

my_str = "hhHHHellO".lower()
samoe_vsterch = None
maximum = 0

for i in set(my_str):
    count = my_str.count(i)
    print(count)
    if count > maximum:
        maximum = count
        samoe_vsterch = i

print(samoe_vsterch)