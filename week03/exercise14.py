'''
Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами.
'''
import turtle as tu
tu.shape('turtle')

def star(a):
    b=180 - (360/a/2)
    n = a
#    tu.forward(100)
#    tu.right(b)
    while n >= 0:
        tu.forward(100)
        tu.right(b)
        n -= 2
    tu.forward(100)
#    tu.right(b)
#    tu.forward(100)

tu.speed('slowest')
tu.penup()
tu.goto(-100,0)
tu.pendown()
a1=5
star(a1)
tu.goto(-100, 0)
tu.penup()
tu.goto(100,35)
tu.pendown()
a2 = 11
star(a2)
tu.right(164)#можно запихнуть в функцию
tu.forward(100)
tu.right(164)
tu.forward(100)
tu.right(164)
tu.forward(100)
tu.goto(100, 35)