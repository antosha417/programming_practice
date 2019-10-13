import turtle

turtle.shape('turtle')

def star(n):
    #turtle.left(180-((n-2)/n*90))
    for i in range(n):
        #turtle.left((n-2)/n*180)
        turtle.forward(100)
        turtle.left((180-(n-2)/n*180)+((n-2)/n*180/3*2))

#a=int(input())
#star(a) - по идее должно быть так, но не работает
star(5)