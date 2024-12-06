L = [1, 2, 3, 4, 5, 1, 2, 3]
L2 = []
L3 = [a for a in L if a not in L2 and L2.append(a)]
print(L2)
# попробовать без апенда