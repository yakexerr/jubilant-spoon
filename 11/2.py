'''
Для каждого слова (слова разделены пробелом) из заданного текста
напечатать, сколько раз оно встретилось заданном тексте.
a. С помощью словаря.
b. С помощью метода setdefault (изучить самим).
c. С помощью класса defaultdict (изучить самим).
d. С помощью класса Counter (изучить самим).
'''
lst = ['Преобразование', 'через', 'метод', 'join()']

#Объединяем элементы списка с пустым разделителем
print(''.join(lst))


#Устанавливаем пробел в качестве разделителя
print(' '.join(lst))
