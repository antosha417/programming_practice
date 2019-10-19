# a = [6, 2, 4, 5, 0, 7, 2, 1, 9, 7, 7, 6, 1, 7]
#      N  N  N  N  N  N  Y  N  N  Y  Y  Y  Y  Y
# a = [6, 7, 4, 4, 2, 2, 8]
#      N  N  N  Y  N  Y  N
a = [5, 8, 2, 8, 5, 0, 9]
#      N  N  N  Y  Y  N  N
n = len(a)
b = set()
for i in range(n):
    if a[i] in b:
        print ('Yes')
    else:
        print('No')
        b.add(a[i])

# снова делаешь за квадрат, сохраняй элементы которы видел во множество, это гораздо эфективнее