n = int(input())
a = []
for i in range(n):
    c = int(input())
    a.append(c)
f = 0
for i in range(n):
    for j in range(n):
        if a[i] == a[j] and i != j:
            f += 1
    if f == 0:
        print(a[i])
    else:
        f = 0