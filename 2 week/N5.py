"""
По данному натуральном n вычислите сумму 1! + 2! + 3! + ... + n!
"""

n = int(input())
sum = 0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += fact
print(sum)