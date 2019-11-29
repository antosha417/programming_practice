n = int(input())
summa = 0
fact = 1
for i in range(1, n + 1):
    fact = i * fact
    fact = i * fact
    summa = summa + fact

print(summa)