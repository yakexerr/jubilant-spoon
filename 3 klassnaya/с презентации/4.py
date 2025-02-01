'''
Из одной строки создать другую ,в которой остаются только буквы английского алфавита
'''

alph = 'ABCDEFJHIGKLMNOPQRSTYVWXUZ'
alph1 = alph.lower()
alph2 = alph1 + alph

s = ''
my_str = "A1b,c d"
for c in my_str:
    if c in alph2:
        s+=c
print(s)
