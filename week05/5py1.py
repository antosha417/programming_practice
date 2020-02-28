def degree(a,n):
    res=1
    for i in range(n):
        res*=a
    return res

a=int(input())
n=int(input())
print(degree(a,n))