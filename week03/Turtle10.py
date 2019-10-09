import turtle

def draw_2circles(step):
    step=10
    Nsteps=30
    for i in range(Nsteps):
        turtle.forward(step)
        turtle.left(360/Nsteps)
    for i in range(Nsteps):
        turtle.forward(step)
        turtle.right(360 / Nsteps)

step=10
nspirals=3
angle=180/nspirals
for i in range(nspirals):
    draw_2circles(step)
    turtle.left(angle)
