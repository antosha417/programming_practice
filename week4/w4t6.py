s = list(map(int, input().split()))
s1 = set()
for elem in s:
    if elem in s1:
        print('YES')
    else:
        print('NO')
    s1.add(elem)