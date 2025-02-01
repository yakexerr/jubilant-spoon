'''
4) вывести индексы всех минимальных эл-ов списка
пример:
[1,2,3,1,4]
Вывод
0, 3
5) Найти самую длинную цепочку по кол-ву слов, в которй первая буква следующего слова - последняя буква предыдущего.
Если таких несколько, вывести ту, в которой больше символов. Если таких несколько, то вывести ту, которая меньше
лексикографически
    Пример: Ab bcd def fh hi
    вывод:

6) в списке матриц найти матрицу с наибольшей суммой
7) найти слово с максимальным количеством
8) в матрице вывести диагональ с максимальной суммой
'''

# 4 (скорее всего надо проходиться по списку и его индексы записывать
# может найти минимальный элемент и все его индексы выписать
sp = [1,2,3,1,4]
minimum = min(sp)
b = [i for i, val in enumerate(sp) if val == minimum]
print(", ".join(map(str, b)))


# 5) сделать список списков, и их сравнивать?
text = "Ab bcd def fh hi"
words = text.split()

# Формирование цепочек
chains = []
for i in range(len(words)):
    chain = [words[i]]
    for j in range(i + 1, len(words)):
        if chain[-1][-1].lower() == words[j][0].lower():
            chain.append(words[j])
    chains.append(chain)

# Поиск максимальной длины цепочки
max_len = max(len(chain) for chain in chains)

# Фильтрация цепочек с максимальной длиной
longest_chains = [chain for chain in chains if len(chain) == max_len]

# Поиск цепочки с максимальным количеством символов
max_chars = max(sum(len(word) for word in chain) for chain in longest_chains)
filtered_chains = [chain for chain in longest_chains if sum(len(word) for word in chain) == max_chars]

# Поиск лексикографически минимальной цепочки
result = min(" ".join(chain) for chain in filtered_chains)

print(result)

# 8)
'''
1 2 3
4 5 6
7 8 9
я думаю сделать цикл, в которм посчитаются обе диагонали и сравнить их
надо из первого списка брать 1-й, из второго второй и тд

matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(matr))
for i in range(len(matr)):
    for j in range(len(matr)):
        print(matr[i])
        '''
