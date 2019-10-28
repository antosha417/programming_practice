'''
Дано действительное положительное число a и целоe число n.
Вычислите a в степени n. Решение оформите в виде функции power (a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
'''


def power(a, n):
    b = 1
    for _ in range(abs(n)):
        b *= a
    if n >= 0:
        return b
    else:
        return 1 / b


a = float(input())
n = int(input())
print(power(a, n))