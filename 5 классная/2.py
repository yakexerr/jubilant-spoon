sp = list("Hello ;")
a = []
sp_l = []

for i in range(len(sp)):
    sp_l.append(sp[i].lower())
    if sp_l[i] not in a:
        a.append(sp_l[i])

for j in range(len(a)):
    if a[j] != " ":
#        print(f"{a[j]} - {sp_l.count(a[j])}")
        print(str(a[j]) + " - " + str(sp_l.count(a[j])))