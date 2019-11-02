def power(a, n):
    s = 1
    if n > 0:
        for i in range(n):
            s *= a
    else:
        m = -n
        for i in range(m):
            s *= (1 / a)
    return s


a0 = float(input())
n0 = int(input())
print(power(a0, n0))
