n = int(input())
factorial = 1
ans = factorial
for i in range(2, n + 1):
    factorial *= i
    ans += factorial
print(ans)
