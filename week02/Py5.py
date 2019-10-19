def sum_factorials(n):
    a=1
    summar=0
    for i in range(1,n+1):
        a=a*i
        summar+=a
    print(summar)

n=int(input())
sum_factorials(n)