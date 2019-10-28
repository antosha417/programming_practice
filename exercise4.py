what = input()
if what == 'not main':
    n = int(input())
    summ: int = 0
    for k in range(n):
        a = input().split()
        for i in range(len(a)):
            a[i] = int(a[i])
        summ += int(a[-k-1])
        k += 1
    print(summ)
else:
    n = int(input())
    summ: int = 0
    for k in range(n):
        a = input().split()
        for i in range(len(a)):
            a[i] = int(a[i])
        summ += int(a[k])
        k += 1
    print(summ)