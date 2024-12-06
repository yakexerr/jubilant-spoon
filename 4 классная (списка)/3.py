s = "Hello"  # Исходная строка
b = []  # Создаем пустой список для символов

# Преобразуем строку в список символов, приводя их к нижнему регистру
for char in s:
    b.append(char.lower())

maximum = 0
samoe_vstrech = None

# Перебираем "символы-кандидаты"
for kand in b:
    count = 0
    # Считаем количество вхождений данного символа
    for n in b:
        if n == kand:
            count += 1
    # Если текущая частота больше предыдущей
    if count > maximum:
        maximum = count
        samoe_vstrech = kand

print(samoe_vstrech)
