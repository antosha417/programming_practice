list0 = list(map(int, input().split()))
dict0 = {}
for i in list0:
    if i not in dict0:
        dict0[i] = 0
for i in list0:
    print(i, end = ' ')
    if dict0[i] == 0:
        print('NO')
    else:
        print('YES')
    dict0[i] += 1