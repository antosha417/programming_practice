n = int(input())
list0 = []
while n != 0:
    list0.append(n)
    n = int(input())
list0.remove(max(list0))
print(max(list0))