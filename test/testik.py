from math import sqrt
print("Вычисление корней квадратного уравнения ax**2 + bx + c = 0")
a = float(input("Введите а "))
b = float(input("Введите b "))
c = float(input("Введите c "))

if a != 0:
    d = b**2 - 4*a*c
    if d > 0:
        x2 = (-b + sqrt(d))/(2*a)
        x1 = (-b - sqrt(d))/(2*a)
        print(x1, x2)
    elif d == 0:
        x1 = -b/(2*a)
        print(x1)

    else:
        print("НЕТ")


if a == 0 and b != 0:
    x = -c / b
    print(x)
else:
    print("НЕТ")

if a == 0 and b == 0 and c != 0:
    print("НЕТ")



# x^2 + 7x + 6.25 = 0
# 1b + 4c = 0 => x + 4 = 0=> x = -4
