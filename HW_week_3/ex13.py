from turtle import *

def draw_arc(r):
    circle(r, 90)

def draw_circle(r):
    circle(r)

def main():
    shape('turtle')
    speed(0)
    pencolor('yellow')
    fillcolor('yellow')
    begin_fill()
    draw_circle(100)
    end_fill()
    x = 30
    for _ in range(2):
        up()
        goto(x, 120)
        down()
        fillcolor('black')
        begin_fill()
        draw_circle(20)
        end_fill()
        x = -30
    r = 50
    speed(1)
    pensize(10)
    for _ in range(2):
        up()
        goto(0,20)
        down()
        pencolor('red')
        draw_arc(r)
        r = -r
        left(90)
    mainloop()
main()