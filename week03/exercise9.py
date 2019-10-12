import  math as math
import turtle as tu
tu.shape('turtle')



def angel(n):
    a = (n - 2) / n * 180
    R = a/2/math.sin(math.pi/n)
    b = math.sqrt((R ** 2 + R**2 - R*R* math.cos(a)))
    while n != 0:
        tu.forward(a)
        tu.left(180 - a)
        n -= 1

n = 3

while n <= 10:
    angel(n)
    tu.penup()
    tu.goto()
    tu.pendown()
    n += 1

