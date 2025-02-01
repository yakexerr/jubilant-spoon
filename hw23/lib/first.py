def triangle_type(a, b, c):
    if (a > 0) and (b > 0) and (c > 0):
        if (a + c > b) and (a + b > c) and (c + b > a):
            if a == b == c:
                return "Равносторонний"
            elif a == b or a == c or c == b:
                return "Равнобедренный"
            else:
                return "Разносторонний"
        else:
            return "Такого треугольника не существует"
    else:
        return "Стороны треугольника должны быть больше нуля"
