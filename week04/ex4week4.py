lst = [1, 4, 2, 2, 3, 1, 10]
for i in range(len(lst)):
    t = lst.count(lst[i])
    if t == 1:
        print(lst[i])


