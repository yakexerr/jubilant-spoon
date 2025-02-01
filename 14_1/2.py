'''
Проверить, что все символы строки с чётными индексами являются
гласными буквами английского алфавита.

'''
s = 'bala'
s1 = 'alalala'
sim = set("aeiouAEIOU")
print(all(s1[i] in sim for i in range(0, len(s1), 2)))
s_ = s1[::2]
print(s_)
print(all(el in sim for el in s_))