""" How many words in text"""

def set_str(a, before):
    for i in range(len(a)):
        if set([a[i]]) & before != set([]):
            pass
        else:
            before.add(a[i])

n = int(input())
before = set([])
for j in range(n):
    a = input()
    a = a.split()
    set_str(a, before)

print(len(before))
