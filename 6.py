a = []
x = int(input())
while x != 0:
    a.append(x)
    x = int(input())
mx = max(a)
a.remove(mx)
print(max(a))