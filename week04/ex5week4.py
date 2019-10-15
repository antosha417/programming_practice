lst1 = [1, 3, 2, 4, 7, 3, 8, 1, 80, 70, 70]
lst2 = [1, 3, 6, 78, 5, 1, 80, 70, 4]
st2 = set(lst2)
st1 = set(lst1)
a = sorted(list(st1 & st2))
for i in range(len(a)):
    print(a[i])

