"""
print elem are in a[] & in b[]
"""

a = input()
a = a.split()
b = input()
b = b.split()
a.sort()
b.sort()
same = []
if len(a) <= len(b):
    n = len(a)
    small = a
    big = b
else:
    n = len(b)
    small = b
    big = a

j = 0
for i in range(0, n):
    while small[i]>=big[j] and j<len(big):
        if small[i] == big[j]:
            same.append(small[i])
        j+=1

print(same)