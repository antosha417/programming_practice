a = []
b = []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b.append(a.count(a[i]))
for i in range(n):
    if b[i] > 1:
        c = a[i]
        while b[i] > 0:
            a.remove(c)
            b[i] -= 1
print(a)