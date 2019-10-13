'''
Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.
'''
import turtle as tu
tu.shape('turtle')

def eight(n):
    tu.circle(n)
    tu.left(180)
    tu.circle(n)
n = 20#радиус окржности
f = 10#количество окружностей
tu.left(90)
while f >= 0:
    eight(n)
    n += 10
    f -= 1