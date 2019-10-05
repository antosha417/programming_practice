def even_index(a):
    evenindex=a[::2]
    print(' '.join([str(elem) for elem in evenindex]))

a=input().split()
even_index(a)