import turtle
import math
turtle.shape('turtle')

for i in range (1,1000,1):
    turtle.left(math.log(i))
    turtle.forward(i/100)