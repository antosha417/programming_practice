list0 = [1, 4, 4, 3, 5, 2, 6, 1, 0, 7, 3]
count = 0
for i in range(1, len(list0)):
    if list0[i - 1] < list0[i] and list0[i] > list0[i +1]:
        count += 1
print(count)