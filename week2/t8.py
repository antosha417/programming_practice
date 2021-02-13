a = []
c = int(input())
while c != 0:
    a.append(c)
    c = int(input())
for elem in a:
    if elem % 2 == 0:
        print(elem)