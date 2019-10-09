def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += factorial(i)
print(ans)
