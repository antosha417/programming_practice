v = 0
t = []
n = int(input())
for i in range(n):
    c = int(input())
    t.append(c)
for i in range(1, n - 1):
    if t[i - 1] < t[i] and t[i] > t[i + 1]:
        v += 1

print(v)
