""" was a[i] before?"""

a = input()
a = a.split()
before = set([])
for i in range(len(a)):
    if set([a[i]]) & before != set([]):
        print('yes')
    else:
        before.add(a[i])
        print('no')

"""print (bool(a[0] == '1'))
print(before & '1')


a = [1, 2, 3, 1, 2, 3]
before = set([])
for i in range(len(a)):
    if set([a[i]]) & before != set([]):
        print('yes', before)
    else:
        print('no', before)
        before.add(a[i])
"""