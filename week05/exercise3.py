# надо ли проверять что существует фигура?
'''
Напишите функцию, которая в зависимости от выбора пользователя вычисляет площадь круга,
прямоугольника или треугольника. Для вычисления площади каждой фигуры должна быть написана отдельная функция.
'''
import helpp as h
print("input the name of figure")
name = input()
if name == 'rtiangle':
    a = int(input())
    b = int(input())
    c = float(input())
    print(h.tr(a, b, c))
elif name == 'square':
    a = int(input())
    b = int(input())
    print(h.sq(a, b))
elif name == 'circul':
    a = int(input())
    print(h.circul(a))
else:
    print('impossible to count')