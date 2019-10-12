n = int(input())
n_general = 0
s_general = []
f, k = 0, 0
for i in range(n):
    s_current = list(map(str, input().split()))
    n_current = len(s_current)
    s_general.append(s_current)
    for j in range(n_current):
        for k in range(n_general + j):
            if s_current[j] == s_general[k]:
                f = 1
        if f == 0:
            k += 1
        f = 0
    n_general += n_current
print(k)