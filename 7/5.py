# просты - делятся на себя и на 1
L = [1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 27, 29 ,41]
L2 = [a for a in L if a%2!=0 and a%4!=0 and a%6!=0 and a%9!=0 and a%10!= 0]
#print(L2)