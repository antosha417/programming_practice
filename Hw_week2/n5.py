from math import *
n = int(input())
s = 0
for i in range(n):
    s += factorial(i + 1)
print(s)