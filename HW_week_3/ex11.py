from turtle import *

def draw_circle(r):
    circle(r)
    right(180)
    circle(r)
def main():
    n = int(input()) #Количество кругов на крыле
    shape('turtle')
    speed(0)
    r = 60
    right(90)
    for i in range(n):
        draw_circle(r)
        r += 5
    mainloop()
main()