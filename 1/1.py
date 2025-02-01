from math import sqrt

a = float(input("Введите коэффицент а: "))
b = float(input("Введите коэффицент b: "))
c = float(input("Введите коэффицент c: "))
diskr = 0
'''
сначала проверить, является ли а 0;
'''


def math(a, b, c):
    if a == 0 and b != 0:
        return (-c) / b
    elif a==0 and b == 0:
        return c
    else:
        diskr = b*b - 4*a*c
        return f"x1: {(-b-sqrt(diskr))/(2*a)}, x2: {(-b+sqrt(diskr))/(2*a)}"


print(math(a,b,c))