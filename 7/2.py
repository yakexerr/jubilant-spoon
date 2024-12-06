L = [1, 2, 3]
L2 = [a for a in L if a % 2 == 0]
if len(L2) > 0:
    print("True")
else:
    print("False")