def was_earlier(row):
    a = set()
    for i in range(len(row)):
        if int(row[i] in a) == 0:
            a.add(row[i])
            print('NO')
        else:
            print('YES')

row = [int(elem) for elem in input().split()]
was_earlier(row)