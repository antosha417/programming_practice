#Нарисуйте 10 вложенных правильных многоугольников. Используйте функцию, рисующую правильный n-угольник.
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    def prmn(n, dlina):
        sumAngle = 180*(n-2)
        Angle = sumAngle/n
        for i in range(n):
            turtle.forward(100)
            turtle.left(180 - Angle)
    for i in range(3, 11):
        prmn(i, 50)