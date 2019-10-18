s = input()
lst = s.split()

ans = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            ans += 1
print(ans)
