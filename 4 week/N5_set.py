"""
print elem are in a[] & in b[], using set
"""
a = input()
a = a.split()
a = set(a)
b = input()
b = b.split()
b = set(b)

print(a&b)