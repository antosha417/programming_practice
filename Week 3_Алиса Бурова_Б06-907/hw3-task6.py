#Нарисуйте паука с n лапами. Пример n = 12:
if __name__ == '__main__':
    n = int(input())
    import turtle
    turtle.shape('turtle')
    for i in range(1, n+1):
        turtle.forward(90)
        turtle.left(180)
        turtle.forward(90)
        turtle.left(180 + 360/n)