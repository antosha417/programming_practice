n = int(input())
sum = 0
fact = 1
for i in range(1, n + 1):
    fact = i * fact
    sum = sum + fact

print(sum)