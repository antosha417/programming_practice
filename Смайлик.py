import turtle

turtle.shape('turtle')

turtle.color("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.goto(-45, 125)
turtle.color("blue")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(45, 125)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 105)
turtle.pendown()
turtle.left(90)
turtle.width(10)
turtle.color("black")
turtle.backward(32)

turtle.penup()
turtle.goto(-45, 55)
turtle.pendown()
turtle.left(200)
turtle.color("red")
turtle.circle(50, 135)