# a = [6, 2, 4, 5, 0, 7, 2, 1, 9, 7, 7, 6, 1, 7]
#      N  N  N  N  N  N  Y  N  N  Y  Y  Y  Y  Y
# a = [6, 7, 4, 4, 2, 2, 8]
#      N  N  N  Y  N  Y  N
# a = [5, 8, 2, 8, 5, 0, 9]
#      N  N  N  Y  Y  N  N
n = len(a)
p = 0
b = 0
for i in range(0, n):
    for k in range(0, i):
        if a[i] == a[k]:
            b += 1
    if b == 0:
        print ('No')
    else:
        print('Yes')
    b = 0