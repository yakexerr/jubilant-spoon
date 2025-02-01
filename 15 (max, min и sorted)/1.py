'''
 Имеется строка английских слов. Они могут быть разделены пробелом или знаком
препинания, а может и так и так. Нужно найти максимальную по длинне строку
'''

st = "sadasfaf afdsaf,aveavwaef:  wefwaefwae, FgarfGAgvf.grkglr"
a = 'qwertyuiopasdfghjklzxcvbnm'
d = ""
# черз списковое включение фор мереписать
for i in st:
    d += i if i in a else " "


    # if i in a:
    #     d+= i
    # else:
    #     d+= " "
print(d)
print(max(d.split(), key=len))