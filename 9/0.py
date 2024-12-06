# создание матрицы (два способа)
# 1
M = 3
N = 4
a = [[0] * N for i in range(M)]
for i in range(M):
    for j in range(N):
        a[i][j] = i*N + j + 1
print(a)

# 2
a = [list(range(i*N + 1, (i + 1)*N + 1))
     for i in range(M)]
print(a)

b = (1, 2)
print(isinstance(b, tuple))