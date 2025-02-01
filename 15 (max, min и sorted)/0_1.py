'''
Есть список пар имя-должность (список списков). Надо отсортировать по должности, потом по имени. Имя должно стоять в начале
'''
sp = [("Джон", "менеджер"), ("Кай","программист"), ("Иван","смм")]
print(sorted(sp)) # по имени
print(sorted(sp, key=lambda pair: (pair[1].lower(), pair[0]))) # по должности



d = [('a', 1), ('b', 2), ('a', 1), ('b', 2)]
print(sorted(d, key=lambda pair: pair[0]))


#  name - pair[0]
# post - pair[1]
#  то что проверякм превым должны писать последним этим способом

print(sorted(sp, key=lambda pair: pair[1]))
print(sorted(sp, key=lambda pair: pair[0]))