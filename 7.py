a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if i % 2 == 0:
        print(a[i])
