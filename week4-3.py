a = []
count = 0
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            count += 1
print(count)