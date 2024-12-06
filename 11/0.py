'''
a = [{'name': 'John', 'salary': 100}, {'name': 'Bob', 'salary': 50}]
b = 100000000000
d = None
for emp in a:
    if b > emp['salary']:
        b = emp['salary']
        d = emp['name']
print(d)


# Задача 1 (c - текущий символ
s = 'asasdasdsd'
# мы создавали списковое включение, тут то же самое, но со словарём
#print({c:s.count(c) for c in s.lower() if c != ' '})

print({c:s.count(c) for i, c in enumerate(s.lower()) if c != ' ' and c not in s[:i]})
'''
# Задача 2
n = int(input())

str = (''.join([str(i) for i in range(1, n +1)]))