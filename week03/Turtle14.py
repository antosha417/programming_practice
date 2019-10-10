import turtle

def draw_star(N,a):
    for i in range(N):
        turtle.forward(a)
        turtle.right(720/N)


n=5
a=100
turtle.left(180-540/n)
draw_star(n,a)