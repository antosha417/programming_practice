#Нарисуйте 10 вложенных квадратов.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    for i in range(1, 10):
        turtle.forward(10*i)
        turtle.left(90)
        turtle.forward(10*i)
        turtle.left(90)
        turtle.forward(10*i)
        turtle.left(90)
        turtle.forward(10*i)
        turtle.penup()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(180)
        turtle.pendown()