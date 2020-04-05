t = [2, 2, 4, 5, 6, 4, 6, 5]
m = 0
for i in range(len(t)):
    if i != 0:
        for n in range(i):
            if t[i] == t[n]:
                m += 1

for i in range(len(t)):
    if i != t[:-1]:
        for v in range(i - 1, 0):
            if t[i] == t[v]:
                m += 1

print(m)