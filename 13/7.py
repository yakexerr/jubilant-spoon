'''
Это из 9го урока треугольник паскаля
        может можно его переписать
'''
def Triangle(M):
    a = [[1] * (i + 1) for i in range(M)]
    for i in range(2, M):  # Начинаем с 3-й строки (индекс 2)
        for j in range(1, i):  # Пропускаем первую и последнюю позиции
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return a

# Вывод треугольника
# def Print(a):
#     for r in a:
#         print(" ".join(map(str, r)))
M = 7 # количество строк
triangle = Triangle(M)
for row in triangle:
    # map'ом центруем каждую строку
    k = ' '.join(map(str, row)).center(M*3)
    print(k)
# Print(triangle)

