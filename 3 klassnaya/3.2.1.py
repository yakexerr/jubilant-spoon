# Вычислить, сколько раз в заданном тексте встречается заданный
# символ без учёта регистра.

stroka = 'asdfg'#input()
stroka = stroka.lower()
bukva = 'a'#input()
bukva = bukva.lower()

k = 0
for c in stroka:
    if c == bukva:
        k += 1
print(k)