import turtle

turtle.shape('turtle')

turtle.right(90)
for i in range (10):
    turtle.circle(45+i*5)
    turtle.circle(-45-i*5)