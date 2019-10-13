list0 = [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
counter = 0
for i in range(len(list0) - 1):
    for j in range(i + 1, len(list0)):
        if list0[i] == list0[j]:
            counter += 1
print(counter)