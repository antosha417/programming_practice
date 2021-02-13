# Дано действительное положительное число a и целоe число n. Вычислите a в степени n.
# Решение оформите в виде функции power (a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.
# (pythontutor.ru, 8 урок, отрицательная степень)
from math import ceil

num = 0
def checknum(num):
    """присваивает переменной num значение float с ввода """
    _ = 1
    while _:
        try:
            num=float(input())
        except ValueError:
            print('введите число (по-одному)')
        _=0
    return num

def checknumf(num):
    """присваивает переменной num значение положительного float числа с ввода """
    _ = 1
    while _:
        try:
            num=float(input())
        except ValueError:
            print('введите число (по-одному)')
        else:
            if num >= 0:
                _=0
            else:
                print('введите положительное число')
    return num

def checknumint(num):
    """присваивает переменной num значение положительного int числа с ввода """
    _ = 1
    while _:
        try:
            num=int(input())
        except ValueError:
            print('введите целое число')
        else:
            if num >= 0:
                _=0
            else:
                print('введите положительное число')
    return num

def power (a,n):
    ''' возводит число а в степень n'''
    x=1
    if n>0:
        for i in range(n):
            x*=a
    elif n<0:
        for i in range(n*(-1)):
            x/=a
    return x #проверку на ноль не делаем, там останется единица

if __name__ == '__main__':
            print('Возведение числа в степень.')
            print('Введите основание степени (действительное положительное число):')
            a=checknumf(num)
            print('Введите степень (целое число):')
            n=int((checknumint(num)))
            print('a^n=', power(a,n))
