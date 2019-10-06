import turtle
turtle.shape('turtle')
i=1
numsteps=100
while i<=numsteps:
    turtle.left(360/numsteps)
    turtle.forward(5)
    i+=1