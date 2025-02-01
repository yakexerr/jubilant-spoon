'''
Реализовать функцию split_thousands(text), которая возвра-
щает строку и добавляет в качестве разделителя тысяч неразрыв-
ный пробел (символ с кодом 160).
Пример
split_thousands('Hello 123 world 1234 -12345678.')
# → 'Hello 123 world 1 234 -12 345 678.'
'''
import re


def split_thousands(text):
    a = re.sub(r'(\d(?=(\d{3})+\b))', r'\1'+chr(160), text, flags=re.I)
    return a

print(split_thousands('Hello 123 world 1234 -12345678.'))