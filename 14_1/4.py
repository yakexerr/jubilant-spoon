'''
Проверить с помощью all (без множеств и словарей), что список длины
n содержит все числа от 1 до n (по одному разу).
'''
n = 4
sp = [1, 2, 3, 4] # n = 4

print(all([i+1 in sp for i in range(n)]))