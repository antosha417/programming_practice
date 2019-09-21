n = int(input("Число:"))
sum = 0
a = 1
for i in range(1, n+1):
    a *= i
    sum += a
print(sum)