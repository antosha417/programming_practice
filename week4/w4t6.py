a = []
s = list(map(int, input().split()))
f = 0
for i in range(len(s)):
    for j in range(i):
        if s[i] == s[j]:
            f = 1
    if f == 1:
        print('YES')
    else:
        print('NO')
        f = 0