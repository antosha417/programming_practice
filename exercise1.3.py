'''
Даны три числа. Выведите значение наименьшего из них.
'''
a = int(input())
b = int(input())
c = int(input())
if a<=c and a<=b:
    print(a)
else:
    if b<=c and b<=a:
        print(b)
    else:
        if c<=a and c<=b:
            print(c)