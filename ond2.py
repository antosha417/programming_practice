l = []
n = int(input())
while n != 0:
    l.append(n)
    n = int(input())
for i in range(len(l)):
    if l[i] % 2 == 0:
        print(l[i])