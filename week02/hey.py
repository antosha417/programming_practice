t = []
n = int(input())
for i in range(n):
    c = int(input())
    t.append(c)
print(t)
minimum, maximum = t[0], t[0]
max_i, min_i = 0, 0
for i in range(n):
    if t[i] > maximum:
        maximum = t[i]
        max_i = i
    if t[i] < minimum:
        minimum = t[i]
        min_i = i
t[max_i], t[min_i] = t[min_i], t[max_i]

print(t)
