t = []
n = int(input())
for i in range(n):
    c = int(input())
    t.append(c)

m = []
j = int(input())
for i in range(j):
    f = int(input())
    m.append(f)

A = set(t)
B = set(m)
C = A & B
C = sorted(C)
print(C)