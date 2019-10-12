a, b = [], []
na = int(input())
nb = int(input())
for i in range(na):
    c= int(input())
    a.append(c)
for i in range(nb):
    c = int(input())
    b.append(c)
a_b = []
for i in range(na):
    for j in range(nb):
        if a[i] == b[j]:
            a_b.append(a[i])
for i in range(len(a_b)):
    for j in range(i, len(a_b)):
        if a_b[i] > a_b[j]:
            c = a_b[j]
            a_b[j] = a_b[i]
            a_b[i] = c
print(a_b)