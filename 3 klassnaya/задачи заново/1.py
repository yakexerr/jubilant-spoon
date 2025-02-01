'''
Вычислить, сколько раз в заданном тексте встречается заданный
символ без учёта регистра.
Исходные данные:
HeLlo
L
Результат:
2
'''

my_str = 'HellOO'
my_str_lower = my_str.lower()
count = 0

for i in range(len(my_str)):
    if "L".lower() == my_str_lower[i]:
        count += 1

print(count)