def even_elems(lst):
    for elem in lst:
        if int(elem) %2==0:
            print(elem,end=' ')

arr=input().split()
even_elems(arr)
