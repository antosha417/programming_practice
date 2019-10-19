n = 3
# n - сколько строк в словаре
a = {}
for i in range(n):
    s = input()
    b = s.split()
    a[b[0]] = b[1]
wordd = input()
for key in a:
    if a[key] == wordd:
        print(key)