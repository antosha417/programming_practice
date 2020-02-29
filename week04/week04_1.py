s = input()
lst = s.split()
ans = 0
for i in range(1, len(lst) - 1):
    if lst[i] > lst[i + 1] and lst[i] > lst[i - 1]:
        ans += 1
print(ans)
