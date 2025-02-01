m = [
    [1, 2, 3, 4],
    [-56, 78, 9, 0]
]
max = -1
# нужно подмтроиться под каждый столбец, у меня в каком-то отступ 1, в каком-то 2 и тд ,надо чтоб везде 1 был (
# смотри пример вывода в 13 уроке на странице 16
for i in range(len(m)):
    for j in range(len(m)):
        if max < len(str((m[i][j]))):
            max = len(str((m[i][j])))
print(max)

print("------")
for i in m:
    k = ' '.join([str(n).ljust(max) for n in i])
    print(k)