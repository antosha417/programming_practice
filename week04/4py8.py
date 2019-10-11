def synonim(n):
    syn = dict()
    for i in range(n):
        a, b = input().split()
        syn[a] = b
        syn[b] = a
    print(syn.get(input()))

N = int(input())
synonim(N)