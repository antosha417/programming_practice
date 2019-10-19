a = []
k = 0
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(1, n - 1):
    if a[i] >  a[i - 1] and a[i] > a[i + 1]:
        k += 1
print(k)