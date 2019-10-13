'''
Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность.
'''
import turtle as tu
tu.shape('turtle')
# первый вариант
#n=6
#a = 360/n
#while n != 0:
#    tu.circle(50)
#    tu.right(a)
#    n -= 1
def eight(n):
    tu.circle(n)
    tu.right(180)
    tu.circle(n)
n = 50#радиус окружности
f = 6# количесво окружностей
r = 360/f
while f != 0:
    eight(n)
    tu.right(r)
    f-=2