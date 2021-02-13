a = []
c = int(input())
while c != 0:
    a.append(c)
    c = int(input())
max_a = 0
max2_a = 0
for i in range(len(a)):
    if a[i] > max_a:
        max_a = a[i]
for i in range(len(a)):
    if a[i] > max2_a and a[i] != max_a:
        max2_a = a[i]
print(max2_a)