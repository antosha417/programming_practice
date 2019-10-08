a = []
s0 = input()
f = int(s0)
for i in range(0, f):
    s = input()
    b = s.split()
    a = a + b
n = len(a)
d = 0
q = 0
for i in range(0, n):
    if a[i] == a[0]:
        q += 1
# q - сколько раз встречается первое слово
u = a[0]
for i in range(0, n):
    for k in range(0, n):
        if a[i] == a[k]:
            d += 1
    if d > q:
        q = d
        u = a[i]
    d = 0
# q - сколько раз встречается максимум u - самый частый элемент
for i in range(0, n):
    for k in range(0, n):
        if a[i] == a[k]:
            d += 1
    if a[i] > u and q == d:
        u = a[i]
    d = 0
print(u)