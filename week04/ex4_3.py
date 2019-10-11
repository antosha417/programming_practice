lst = [1, 1, 1, 2, 2, 1]
m = 0
for i in range(len(lst)):
    if i != 0:
        for a in range(i):
            if lst[i] == lst[a]:
                m += 1



for i in range(len(lst)):
    if i != len(lst):
        for b in range(i + 1, len(lst)):
            if lst[i] == lst[b]:
                m += 1


print(m/2)