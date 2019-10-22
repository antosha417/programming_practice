#3Напишите функцию, которая в зависимости от выбора пользователя вычисляет площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.
c=['круг','Круг','круга','Круга','circle','rheu','rheuf']
rec=['прямоугольник','Прямоугольник','Прямоугольника','прямоугольника','rectangle','ghzvjeujkmybr','ghzvjeujkmybrf']
t=['треугольник','Треугольник','Треугольника','треугольника','triangle','nhteujkmybr','nhteujkmybrf']
def circle_area(r):
    from math import pi
    s=pi*(r*r)
    return s
def rectangle_area(a,b):
    s=a*b
    return s
def triangle_area(x,h):
    s=x*h/2
    return s
print('Введите площадь какой фигуры вы хотите найти:круга,прямоугольника или треугольника')
shape=input()
if shape in c:
    print('Введите радиус круга')
    r=float(input())
    print('Площадь круга равна', round(circle_area(r),2))
if shape in rec:
    print('Введите длины сторон прямоугольника')
    a,b = float(input()),float(input())
    print('Площадь прямоугольника равна', round(rectangle_area(a,b),2))
if shape in t:
    print('Введите длину стороны треугольника и длинну высотыб проведенной к этой стороне')
    x,h = float(input()),float(input())
    print('Площадь треугольника равна', round(triangle_area(x,h),2))
