lst = [10, 3, 2, 4, 5, 1, 7, 6, 8, 9]
M = lst[1]
for i in range(len(lst)):
    if lst[i]>M:
        M = lst[i]
m = lst[1]
for i in range(len(lst)):
    if lst[i]<m:
        m = lst[i]

for i in range(len(lst)):
    if lst[i]==M:
        lst[i]=m
    elif lst[i]==m:
        lst[i]=M

print(lst) #имеется второе решение далее, чтоб Вам точно понравилось

lst1 = [10, 3, 2, 4, 15, 13, 7, 6, 8, 9]
k = 0
j = 0
M = lst1[1]
for i in range(len(lst1)):
    if lst1[i]>M:
        M = lst1[i]
        k = i
m = lst1[1]
for i in range(len(lst1)):
    if lst1[i]<m:
        m = lst1[i]
        j = i

lst1[k], lst1[j] = lst1[j], lst1[k]
print(lst1)
