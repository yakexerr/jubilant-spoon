eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in lst2:
    print(item)
print("-"*10)
print(range(10))
print(list(range(10)))
for i in range(10):
    print(i)

cats = ["Барсик", "Мурзик", "Вася"]
#enumerate возвращает список с парами, где превый элемент - индекс, а второ - значение
print(list(enumerate(cats)))
for idx, cat in enumerate(cats):
    print(f"{idx}. {cat}")

#reversed - перепорачивает строку
print(list(reversed(cats)))
#sorted() - сортирует (в нашем случае по алфавиту
print(list(sorted(cats)))

print("-"* 10)

# циклы со словарями
# items - метож ,позволяющий перебирать словарь по ключам и значениям
for key, value in eng_rus_dict.items():
    print("ключ", key, "значение", value)

i = 0
while i != 5:
    i += 1
print(i)

print("а", ord("а"))
stat_symbol_number = ord("а")
while stat_symbol_number <= ord("я"):
    print(stat_symbol_number, chr(stat_symbol_number))
    stat_symbol_number += 1

