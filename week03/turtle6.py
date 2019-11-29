import turtle

turtle.shape('turtle')
for i in range(12):
    turtle.forward(50)
    turtle.stamp()
    turtle.goto(0,0)
    turtle.right(360/12)
turtle.done()