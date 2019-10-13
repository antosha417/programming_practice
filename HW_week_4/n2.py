list0 = [1, 4, 5, 73, 3, 6, 0, 12]
list_max = max(list0)
list_min = min(list0)
for i in range(len(list0)):
    if list0[i] == list_max:
        i_max = i
    if list0[i] == list_min:
        i_min = i
list0[i_max], list0[i_min] = list0[i_min], list0[i_max]
print(list0)