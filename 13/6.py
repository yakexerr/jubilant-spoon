'''
m = [
    [1, 2, 3, 4],
    [-56555, 78, 9, 0]
]
max = -1
for i in range(len(m)):
    for j in range(len(m)):
        if max < abs(m[i][j]):
            max = abs(m[i][j])
print(max)
max_1 = len(str(max))
for i in m:
    k = ' '.join([str(n).ljust(max_1 + 2) for n in i])
    print(k)

    Это просто вывод массива с ljust, может можно использовать?
'''
# s - сколько?
# width - чем?
def my_ljust1(s, width):
