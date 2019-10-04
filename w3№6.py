import turtle

turtle.goto(0, 0)
n= int(input())
k=360/n
turtle.shape('turtle')
for i in range(n):
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(k)