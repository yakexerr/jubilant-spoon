'''
def mysum(*args):
    print(sum(args))


mysum(1, 2)
mysum(1, 2, 3)


# def add(a, b):
def add(*args):
    print(sum(args))


# a, b = [int(d) for d in input().split()]
# add(a, b)

a = [int(d) for d in input().split()]
add(*a) #add(a[0], a[1], ....)
'''
array = [1, 2, 3]
print(*array)
print(*array, sep="; ")

s = 'abc'
print(list(zip(array, s, range(5, 20, 7))))
print(list(zip(array)))

print('----')

print(list(zip([1, 2, 3, 4],
               'abc')))  # по длинне ориентируется на самую малую коллекцию, то есть в малой у нас 3, тут он и остановится
# print(list(zip([1, 2, 3, 4], 'abc', strict=True))) # ошибку даст


# zip можно использовать для транспонирования матриц
m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(list(zip(*m)))
print([list(col) for col in zip(*m)])

# новое
from itertools import count, cycle, accumulate, chain, dropwhile


def my_enumerate(seq, start=0):
    return zip(seq, count(start))


print(list(my_enumerate("abc", 1)))


def shift(char, shift_size):  # шифр Цезаря
    return ...  # воделать самому (для большого и малого регистра!)


shifts = [10, 7, 3]
zip(s, cycle(shifts))
# ''.join([shift(c, shifts) for c, shifts in zip(s, cycle(shifts))])

a = [['Bob', 7], ["Alice", 20]]
print(sorted(a, key=lambda p: p[1]))

print(list(accumulate([1, 2, 3, 4, 5], min)))

print('----')

# ф-я для того, чтобы посчитать, когда готово будет кофе, если минута на то, чтобы вязть заказ и минута на готовку
# initial - то, c чего начинается (типа к первому значению добавляется initial)
a = accumulate([1, 2, 3, 4, 5], lambda perv_res, cur: perv_res + 1 + cur, initial=1)
print("time ", list(a))

m = [[1, 2], [3, 4], [5, 6]]
print(list(chain(*m)))

# sudoku
# ф-ии сам
# [for nine in chain(all_rows(m), all_cols(m), all_squares(m))]

def mycompress(seq, flags): # это про chain.from_iterable()
    return (item for item, flag in zip(seq, flags))


for c in dropwhile():