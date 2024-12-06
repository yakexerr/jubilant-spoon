# .strip() - удаляет пробелы с двух сторон строки
#ord пробела = 32

#stroka = input()
stroka = "    ddd "
i = 0
s = len(stroka) - 1 # последний символ в строке

# слева
while i <= s and stroka[i] == " ":
    i += 1

#справа
while s >= i and stroka[s] == " ":
    s -= 1

# рез без пробелов в нач и в кон
print(stroka[i:s + 1])

