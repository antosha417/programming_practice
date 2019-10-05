def sum_factorials(n):
    a=1
    sum=0
    for i in range(1,n+1):
        a=a*i
        sum+=a
    print(sum)

n=int(input())
sum_factorials(n)