a = []
a1 = 0
a2 = 0
n = int(input())
for i in range(n):
    a.append(int(input()))
b = max(a)
c = min(a)
for i in range(n):
    if a[i] == b:
        a1 = i
    if a[i] == c:
        a2 = i
a[a1], a[a2] = a[a2], a[a1]
print(a)