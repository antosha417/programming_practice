"""
print unikal elem
"""

a = input()
a = a.split()
flags = [1] * len(a)    #arr of unikality
for i in range(0, len(a)):
    flag = 1
    for j in range(i+1, len(a)):
        if a[i]== a[j]:
            flags[i] = 0
            flags[j] = 0
for i in range(0, len(a)):
    if flags[i] == 1:
        print(a[i], end = ' ')