def was_earlier(row):
    a = set()
    for i in range(len(row)):
        if row[i] in a:
            print('YES')
        else:
            a.add(row[i])
            print('NO')

row = [int(elem) for elem in input().split()]
was_earlier(row)
