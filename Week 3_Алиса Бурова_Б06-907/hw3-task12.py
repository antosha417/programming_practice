#Нарисуйте пружину. Используйте функцию, рисующую дугу.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    turtle.left(90)
    for j in range(10):
        for i in range(180):
            turtle.forward(1)
            turtle.right(1)
        for i in range(180):
            turtle.forward(0.25)
            turtle.right(1)