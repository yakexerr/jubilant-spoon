# первый способ
s = 'текст!'
def count(s, c):

    return s.count(c)
vkl = {c: count(s, c) for i, c in enumerate(s.lower()) if c != " " and c not in s[:i]}
'''
val = list(vkl.values())
keys = list(vkl.keys())

for i in range(len(vkl)):
    print(keys[i], val[i])
    

# третий способ 
    
for k, v in vkl.items():
    print(k, v)
'''
# четвёртый способ

d = {}

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

for k, v in d.items():
    print(k, v)