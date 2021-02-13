n = int(input("ножки: "))
import turtle

turtle.shape('turtle')
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180 - 360/n)


