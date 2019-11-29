def num_dif_words(N,row):
    a = set()
    count = 0
    for i in range(N):
        for elem in row:
            a.add(elem)
    print(len(a))

num = int(input())
lst = set(input().split())
num_dif_words(num,lst)