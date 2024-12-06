

stroka = input()

stroka = stroka.lower() # в нижний регистр
stroka = stroka.replace(' ', '') # удаляю пробелы в строке вводимой
i = 0
s = ""
for i in range(len(stroka) - 1, -1, -1):
    s += stroka[i]

if stroka == s:
    print("Да")
else:
    print("Нет")

#print(s)
#print(stroka)
