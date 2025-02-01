'''
Реализовать функцию vowel_2_index(text), которая заменяет
все гласные буквы на их индексы без учёта регистра.
Пример
vowel_2_index('this Is my string')
# → 'th3s 6s my str15ng'
vowel_2_index('bcd') # → 'bcd'
vowel_2_index('') # → ''
'''
import re


def matches(match):
    return str(match.start(0) + 1) 


def vowel_2_index(text):
    match = re.sub(r'[eyuioa]', matches, text, flags=re.I)

    return match


print(vowel_2_index("this Is my string"))