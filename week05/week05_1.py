"""Дано действительное положительное число a и целоe число n. Вычислите a в степени n.
Решение оформите в виде функции power (a, n). Стандартной функцией возведения в степень
пользоваться нельзя. (pythontutor.ru, 8 урок, отрицательная степень)"""
def power(a, n):
    if n == 0:
        print(1)

    if n > 0:
        prod = a
        flag = 1
        while flag != n:
            prod = prod * a
            flag += 1
        print(prod)

    if n < 0:
        prod = a
        flag = 1
        while flag != -n:
            prod = prod * a
            flag += 1
        print(1/prod)


a = float(input())
n = int(input())
power(a, n)