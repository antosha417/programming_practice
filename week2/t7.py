a = []
c = int(input())
while c != 0:
    a.append(c)
    c = int(input())
for i in range(len(a)):
    if i % 2:
        print(a[i])