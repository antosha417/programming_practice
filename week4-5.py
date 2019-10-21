a = []
b = []
n = int(input())
for i in range(n):
    a.append(int(input()))
    b.append(int(input()))
a = set(a)
b = set(b)
print(a, b)
c = set.intersection(a, b)
с = list(c)
print(c)