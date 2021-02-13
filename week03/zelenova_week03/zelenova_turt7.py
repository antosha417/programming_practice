#7 Спираль
k=1 #cмещение точки по лучу
rfi=0.1 #угол поворота в радианах
dfi=rfi*180/3.14 #угол поворота в градусах
import turtle
turtle.shape('turtle')
for i in range (400):
    ro=k*rfi #приращение спирали
    turtle.forward(ro)
    turtle.left(dfi)
    rfi+=0.1
    ro+=ro