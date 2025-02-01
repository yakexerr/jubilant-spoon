'''
Проверить, что хотя бы один символ строки с нечётным индексом
является согласной буквой английского алфавита.

хотя бы один => any
'''

s = 'kola'
s1 = 'abal'
sim = "bcdfghjklmnvwxz"
print(any((s[i].lower() in sim for i in range(1, len(s), 2))))