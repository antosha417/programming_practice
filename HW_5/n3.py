from math import pi
from math import sqrt

def circle(r):
    return pi * r ** 2

def rectangle(a, b):
    return a * b

def triangle(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    print("Что вы хотите посчитать?\n1. Площадь круга\n2. Площадь прямоугольника\n3. Площадь треугольника")
    t = 1
    while t:
        try:
            n = int(input("Введите номер варианта: "))
        except ValueError:
            print("Попробуйте еще раз")
        else:
            if n in [1, 2, 3]:
                t = 0
            else:
                print("Попробуйте еще раз")
    t = 1
    if n == 1:
        while t:
            try:
                r = float(input("Введите радиус: "))
            except ValueError:
                print("Попробуйте еще раз")
            else:
                if r >= 0:
                    t = 0
                else:
                    print("Попробуйте еще раз")
        print(circle(r))
    elif n == 2:
        while t:
            try:
                list_one = list(map(float, input("Введите стороны: ").split()))
            except ValueError:
                print("Попробуйте еще раз")
            else:
                if len(list_one) == 2 and list_one[0] > 0 and list_one[1] > 0 :
                    t = 0
                else:
                    print("Попробуйте еще раз")
        print(rectangle(list_one[0], list_one[1]))
    else:
        while t:
            try:
                list_one = list(map(float, input("Введите стороны: ").split()))
            except ValueError:
                print("Попробуйте еще раз")
            else:
                if len(list_one) == 3 \
                        and (list_one[0] < list_one[1] + list_one[2])\
                        and (list_one[1] < list_one[0] + list_one[2])\
                        and (list_one[2] < list_one[0] + list_one[1]):
                    t = 0
                else:
                    print("Попробуйте еще раз")
        print(triangle(list_one[0], list_one[1], list_one[2]))
main()