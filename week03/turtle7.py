import turtle

turtle.shape('turtle')
turtle.speed(10)
for i in range(10*100):
    turtle.forward(1+i/100)
    turtle.left(360/100)


turtle.done()