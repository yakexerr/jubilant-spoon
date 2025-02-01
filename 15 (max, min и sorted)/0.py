'''
Общий синтаксис min max и sorted
Из названия собственно и понятно

min(n1,n2,...)
min(1,2) -> вывод: 1
max(1,2) -> вывод: 2


'''

n = [1, 2, 3, 4, 5, 6, 7]
print(min(n))
print(max(n))
print(max("A", "b", "D")) # вывод: b

def myMax(collection):
    # тут ещё по хорошему бы сделать проверку пустой ли список
    m = collection[0]
    for a in collection:
        m = max(m,a)
    return m

a = [1,2,3]
print(max(set(a), set(n))) # на множествах как работает? если все элементы одного входять в другой и в другом есть еще другие, то это множество считаеся большим



print("----------------------")

# sorted принимает только эл-ты коллекции
# referse показывает в какую сторону сортируем False - в порядке возрастания, True - убывания
b = [2, 4, 1, 5]
print(sorted(b, reverse=True))


numbers = [1, 2, -3]
print(max([abs(n) for n in numbers])) # самое большое число по модулю

st = ['hello', 'hi']
print(max([len(s) for s in st])) # самая длинная строка

numbers = [1, 2, -3]
print(max([len(str(n)) for n in numbers])) # самое "длиное" число

print("__")

m = [[1,2], [-3, 4]]
print(max([len(str(n)) for row in m for n in row])) # самое "длинное" число в матрице

print(max([max(row) for row in m])) # самое большое число в матрице

# key= передаётся ссылка на функцию (в нашем случае будет вызываться длинна, то есть максимум среди коючей и выводится слово)
# то есть возвращаем значение по ключу (ВАЖНО!!! юез скобок в ключ писать)
print(max(st, key=len)) # самая длинная строка

print("__")

st2 = ["A", "b", "D"]
print(max(st2, key=len))

# если хотим сделать поиск самого длинного слова без учёта регистра, а ввотзвращалось со всеми регистрами
def lower(s):
    return s.lower()
print(max(st2, key=lower)) # просто lower - метод ,а в ключ можем передавать только функции

# вывод меньшего лексикографически?
st3 = ["AF", "b", "DE"]
def by_len_and_lexi(s):
    return (-len(s), s)
print(min(st3, key=by_len_and_lexi))

print("__")
# ищем индекс максимального значения
numbers = [1, 2, -3]
def abs2(i):
    return abs(numbers[i])
print(max(range(len(numbers)), key=abs))
# чтобы не писать каждый раз новую функцию будем использовать лямбды
print(max(range(len(numbers)), key=lambda i: abs(numbers[i])))

# ещеё способ ,но тут мы не используем тех приколов, получаем картеж и распаковываем
_, _, max_index = max([(abs(n), -i, i) for i,n in enumerate(numbers)])
print(max_index)

print("__")

# sorted тоже имеет key

print(sorted(["hello", "hi"]))
print(sorted(["hello", "hi"], key=len)) # по длинне

print("__")
# posts = ["manager", "CEO", "programmer"]
# a = ["manager", "CEO", "programmer", [{'name': 'John John', 'post' : 'manager'}, {'name': 'Bob', 'post': 'programer'}]]
# sorted([d for d in a, key=lambda d: posts.index(d['post'])])