def num_dif_words(N):
    a = set()
    count = 0
    for i in range(N):
        lst = input().split()
        for elem in lst:
            a.add(elem)
    print(len(a))


num = int(input())
num_dif_words(num)
