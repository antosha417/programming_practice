#Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    for j in range(1, 10):
        for i in range(360):
            turtle.forward(0.6+j*0.2)
            turtle.left(1)
        for i in range(360):
            turtle.forward(0.6+j*0.2)
            turtle.right(1)
