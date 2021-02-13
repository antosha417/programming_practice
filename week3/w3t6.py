import turtle

n = int(input())
turtle.shape('turtle')
for i in range(n):
    turtle.forward(70)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(70)
    turtle.left(180 - 360 // n)