'''
Нарисуйте спираль.
'''
import turtle as tu
tu.shape('turtle')


def half(x, end):
    while x != end:
        tu.circle(x,180)
        x += 10

x = int(input()) #Начальный радиус полуокружности
end = int(input()) #конечный радиус полуокружности
half(x, end)