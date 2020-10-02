def num_single(a):
    flag = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                flag = -1
                break
        if flag > 0:
            print(a[i])
        flag = 1

arr = [int(s) for s in input().split()]
num_single(arr)
