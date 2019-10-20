n = int(input())
a = {}
for i in range(n):
    key = str(input())
    if key in a:
        a[key] += 1
    else:
        a[key] = 1
for key in a:
    if a[key] == 1:
        print(key)