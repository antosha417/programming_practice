import turtle

def circle(n, *, direction):
    if direction == 'left':
        for i in range(180):
            turtle.forward(n)
            turtle.left(2)
    else:
        for i in range(180):
            turtle.forward(n)
            turtle.right(2)

turtle.shape('turtle')
turtle.left(90)
length = 0
for i in range(1, 11):
    length += 0.5
    circle(length, direction = 'left')
    circle(length, direction = 'right')