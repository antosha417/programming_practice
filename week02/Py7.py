def even_index(a):
    evenindex = []
    for i in range(0,len(a),2):
        evenindex.append(a[i])
    print(' '.join(evenindex))

a = input().split()
even_index(a)
