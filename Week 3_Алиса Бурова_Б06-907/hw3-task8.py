#Нарисуйте «квадратную» спираль.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    for i in range(1, 80):
        turtle.forward(i*10)
        turtle.left(90)