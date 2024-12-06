# Вычислить и напечатать, сколько раз в заданном тексте встреча-
# ются гласные буквы.

stroka = input()
glasn = "уеыаоэяиюё"

k = 0
for c in stroka.lower():
    if c in glasn:
        k += 1

print(k)