def sort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                c = a[i]
                a[i] = a[j]
                a[j] = c
    return(a)


a = set(input().split())
b = set(input().split())
print(sort(list(a.intersection(b))))