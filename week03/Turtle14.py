import turtle

def draw_star(N,a):
    for i in range(N):
        turtle.forward(a)
        turtle.right(720/N)


n=5
a=100
dangle=180-540/n #угол-поправка на направление черчения
turtle.left(dangle)
draw_star(n,a)
#turtle.penup()
#turtle.right(dangle)
#turtle.forward(2*a)
#n=11
#turtle.left(dangle)
#turtle.pendown()
#draw_star(n,a)