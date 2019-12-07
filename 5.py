import math
n = int(input())
k = 0
while n != 0:
    k += math.factorial(n)
    n -= 1
print(k)