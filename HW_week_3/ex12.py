from turtle import *

def draw_arc(r1, r2):
    circle(r1, 180)
    circle(r2, 180)
def main():
    right(90)
    r1 = int(input())
    r2 = int(input())
    shape('turtle')
    speed(0)
    for _ in range(5):
        draw_arc(r1, r2)
    mainloop()
main()