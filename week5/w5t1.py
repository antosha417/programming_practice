def power(a, n):
    a1 = 1
    if n > 0:
        for i in range(n):
            a1 *= a
    elif n < 0:
        for i in range(abs(n)):
            a1 /= a
    return(a1)

a, n = map(int, input().split())
print(power(a, n))