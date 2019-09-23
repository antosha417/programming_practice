def even_or_not(a):
    even_elem = []
    for i in range(0, len(a), 2):
        print(a[i], end=' ')

list = input().split()
even_or_not(list)
