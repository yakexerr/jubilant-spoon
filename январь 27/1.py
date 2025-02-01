'''
Нужно реализовать функцию remove_vowels(text), которая уда-
ляет все гласные буквы.
Пример
remove_vowels('HEllo world.') # → 'Hll wrld.'
'''
import re


def remove_vowels(text):
    a = re.sub(r'[eyuioa]', r'', text, flags=re.I)
    return a

print(remove_vowels('HEllOO world'))