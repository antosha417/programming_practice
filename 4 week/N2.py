"""
min <-> max
"""
a = input()
a = a.split()
M = max(a)
m = min(a)
im = a.index(m)
iM = a.index(M)
a[im] = M
a[iM] = m
print(a)