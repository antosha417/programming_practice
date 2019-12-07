a = []
count = 0
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(2, n):
    if a[i-1] > a[i - 2] and a[i - 1] > a[i]:
        count += 1
print(count)
