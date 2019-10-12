#Нарисуйте спираль.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    t = 0.1
    for i in range(360*5):
        turtle.left(5)
        turtle.forward(t)
        t+=0.01