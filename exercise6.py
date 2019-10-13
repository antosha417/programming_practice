'''
Нарисуйте паука с n лапами.
'''
import turtle as tu
tu.shape('turtle')

n = int(input())
a = 360/n
while n != 0:
    tu.forward(50)
    tu.stamp()
    tu.backward(50)
    tu.right(a)
    n-=1