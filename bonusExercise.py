'''
Посчитать сколько раз встречается каждое слово в тексте
'''
from collections import defaultdict as dd

d = dd(lambda: 0)
s = input()
cc = (':', ',', '.', ';', '!',)
for c in cc:
    s = s.replace(c, '')
for val in s.strip().split():
    d[val] += 1

for val in d:
    print(val, d[val])