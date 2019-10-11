#Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    turtle.speed(10)
    for j in range(1, 4):
        for i in range(360):
            turtle.forward(1)
            turtle.left(1)
        turtle.left(180)
        for i in range(360):
            turtle.forward(1)
            turtle.left(1)
        turtle.left(180+60)
