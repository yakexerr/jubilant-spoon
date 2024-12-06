#В целочисленном списке вывести, сколько раз встречается каждое
#число (порядок вывода не важен). Список содержит произвольные
#целые числа.

sp = [1, 2, 3, 3, 1,1,1]
a = []
#b = []
#for i in range(len(sp)):
#    print(f"{sp[i]} - {sp.count(sp[i])}")
for i in range(len(sp)): #прохожусь по данному списку и записываю уникальные в другой список
    if sp[i] not in a:
        a.append(sp[i])

    #b.append(sp.count(sp[i]))
a.sort()
for j in range(len(a)):
    #print(f"{a[j]} - {b[j]} ")
    print(f"{a[j]} - {sp.count(a[j])} ")





