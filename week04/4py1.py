def more_than_neigh(mas):
    count = 0
    for i in range(1, len(mas) - 1):
        if mas[i] > mas[i - 1] and mas[i] > mas[i + 1]:
            count += 1
    print(count)


arr = map(int, input().split())
more_than_neigh(arr)
