t = []
n = int(input())
for i in range(n):
    c = int(input())
    t.append(c)

for i in range(len(t)):
    if t.count(t[i]) == 1:
        print(t[i])