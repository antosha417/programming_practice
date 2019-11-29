def num_pairs(a):
    count = 0
    number = 1
    for i in range(len(a)):
        if a[i] != '':
            for j in range(len(a)):
                if a[i] == a[j] and i != j:
                    number += 1
                    a[j] = ''
            a[i] = ''
            count += number * (number - 1) / 2
            number = 1
    print(count)

arr=[int(s) for s in input().split()]
num_pairs(arr)