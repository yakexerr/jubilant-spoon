from _decimal import Decimal

str = '12345'
print(int(str, base=6) - 5)
a = 15
print(bin(a)[2::])

print(0.1+0.1+0.1 == 0.3)
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1') == Decimal('0.3'))