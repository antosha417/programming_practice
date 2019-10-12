n = int(input())
summary = {}
for i in range(n):
    s = list(map(str, input().split()))
    if summary.get(s[0]) is None:
        summary[s[0]] = {}
    if summary[s[0]].get(s[1]) is not None:
        summary[s[0]][s[1]] += int(s[2])
    else:
        summary[s[0]][s[1]] = int(s[2])
print(summary)