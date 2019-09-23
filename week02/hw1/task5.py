
def sum_fac(x):
    fac = 1
    result = 0
    for i in range(1, x+1):
        fac *= i
        result += fac
    return result
n = int(input())
print(sum_fac(n))
