#Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный многоугольник с большим числом сторон будет выглядеть как окружность.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)