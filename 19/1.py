'''
Найти все номера телефонов, удовлетворяющих шаблону (XXX) XXX-XXXX, и
заменить на формат XXX-XXX-XX-XX.
'''
import re
number = '(937)833-0460'
match = re.sub(r'\((\d{3})\)(\d{3})-(\d{2})(\d{2})', r'\1-\2-\3-\4', number)
print(match)