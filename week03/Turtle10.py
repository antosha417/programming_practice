import turtle

def draw_2circles(Nsteps):
    step=5
    for i in range(Nsteps):
        turtle.forward(step)
        turtle.left(360/Nsteps)
    for i in range(Nsteps):
        turtle.forward(step)
        turtle.right(360 / Nsteps)

N=50
nspirals=3
angle=180/nspirals
for i in range(nspirals):
    draw_2circles(N)
    turtle.left(angle)
