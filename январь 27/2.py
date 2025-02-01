'''
Нужно реализовать функцию remove_vowels2(text), которая
удаляет все гласные буквы внутри слов (первая и последняя буква
не удаляется).
Пример
remove_vowels2('HEllo world.') # → 'Hllo wrld.'
remove_vowels2('A eiu') # → 'A eu'
'''
import re


def remove_volwels2(text):
    a = re.sub(r'\B[eyuioa]\B', r'', text, flags=re.I)
    return a


print(remove_volwels2("A eiu"))
