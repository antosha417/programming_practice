n = int(input())
h = n % (24 * 60) // 60
m = n % 60
print(h, m)