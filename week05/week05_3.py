"""Напишите функцию, которая в зависимости от выбора пользователя вычисляет площадь круга,
прямоугольника или треугольника. Для вычисления площади каждой фигуры должна быть написана отдельная функция."""
import math

def circle(r):
    S = math.pi*r**2
    return S
def rectangle(a, b):
    S = a*b
    return S


def main():
    figure = input('Calculate surface. Choose: circle, triangle, rectangle: ')

    if figure == 'circle':
        r = float(input('Give radius: '))
        print('Surface = ', circle(r))
    if figure == 'rectangle':
        a = float(input('Give 1. side: '))
        b = float(input('Give 2. side: '))
        print('Surface = ', rectangle(a, b))

    if figure == 'triangle':
        a = float(input('Give base: '))
        b = float(input('Give height for base: '))
        print('Surface = ', 0.5*rectangle(a, b))

if __name__== "__main__":
  main()