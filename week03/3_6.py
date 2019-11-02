import turtle
n=int(input())
turtle.shape('turtle')
for i in range(n):
    turtle.left(360/n)
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)