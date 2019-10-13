from turtle import *

def draw_star(n, l):
    angle = 180 / n
    for _ in range(n):
        forward(l)
        left(180 - angle)

def main():
    shape('turtle')
    speed(0)
    l = 100
    draw_star(5, l)
    up()
    goto(-140,0)
    down()
    draw_star(11, l)
    mainloop()
main()