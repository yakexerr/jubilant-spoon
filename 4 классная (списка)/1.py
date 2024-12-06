# вычислить сколько в целочисленном списке встречается данное число

a = [0]
col = int(input("Введите длинну массива: "))
b = int(input("Enter num: ")) # для поиска его
i = 0
k = 0
a = a*col
for i in range(col):
    a[i] = int(input("Entel element: "))
    if a[i] == b:
        k +=1

print(k)