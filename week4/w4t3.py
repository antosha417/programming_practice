n = int(input())
a = []
for i in range(n):
    c = int(input())
    a.append(c)
k = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            k += 1
print(k)