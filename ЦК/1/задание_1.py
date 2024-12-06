lst_plus = []
lst_sub = []
lst_mult = []
lst_div = []
continue_loop = True

while continue_loop == True:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    pmmd = input("Введите операцию: ")
    sum = ''
    mult = ''
    sub = ''
    div = ''
    if pmmd == "+":
        print(f"\nРезультат:\t{num1}+{num2}={num1+num2}\n")
        sum = str(str(num1) + "+" + str(num2) + "=" + str(num1+num2))
        lst_plus.append(sum)
    if pmmd == "-":
        print(f"\nРезультат:\t{num1}-{num2}={num1-num2}\n")
        sub = str(str(num1) + "-" + str(num2) + "=" + str(num1-num2))
        lst_sub.append(sub)
    if pmmd == "/":
        print(f"\nРезультат:\t{num1}/{num2}={num1/num2}\n")
        div = str(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))
        lst_div.append(div)
    if pmmd == "*":
        print(f"\nРезультат:\t{num1}*{num2}={num1*num2}\n")
        mult = str(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
        lst_mult.append(mult)

    print("+:", lst_plus)
    print("-:", lst_sub)
    print("*:", lst_mult)
    print("/:", lst_div)
    print("")

    accept = input("Продолжить? (Введите да/нет): ")
    if accept == "да":
        continue_loop = True
    else:
        continue_loop = False
