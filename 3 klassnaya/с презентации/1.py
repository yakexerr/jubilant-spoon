'''
создать строку взяв из другой только символы с чётным индексом
'''
my_str = 'abcdef'
s = ''
for i in range(len(my_str) - 1):
    if i % 2 == 0:
        s += my_str[i]
print(s)
