n = int(input())
a = []
c = int(input())
a.append(c)
minimum, maximum = c
max_i, min_i = 0
for i in range(n - 1):
    c = int(input())
    a.append(c)
for i in range(n):
    if a[i] > maximum:
        max_i = i
        maximum = a[i]
    elif a[i] < minimum:
        min_i = i
        minimum = a[i]
a[max_i], a[min_i] = a[min_i], a[max_i]