from turtle import *

def draw_circle(r):
    circle(r)
    right(180)
    circle(r)
def main():
    n = int(input()) #Количество лепестков (кратно 2)
    shape('turtle')
    speed(0)
    r = 100
    for i in range(n//2):
        draw_circle(r)
        left(360/n)
    mainloop()
main()