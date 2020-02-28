import turtle
turtle.shape('turtle')
n=12
length=200
for i in range(n):
    turtle.forward(length)
    turtle.stamp()
    turtle.backward(length)
    turtle.left(360/n)