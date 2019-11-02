def degree(a:any, n:any):
    if a.isdigit() and n.isdigit():
        a=int(a)
        n=int(n)
        res = 1
        for i in range(n):
            res *= a
        return res
    else:
        print('Type int variables')


a = input()
n = input()
print(degree(a, n))
