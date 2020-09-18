def power(a: float, n: int):
    if n == 0:
        return 1
    elif n > 0:
        ans1 = 1
        for _ in range(n):
            ans1 *= a
        return ans1

    elif n < 0:
        ans2 = 1
        for _ in range(abs(n)):
            ans2 *= a
        return 1 / ans2


if __name__ == '__main__':
    a = int(input())
    n = int(input())
    print(power(a, n))
