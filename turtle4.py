import turtle as t
n = int(input())
k = n
t.left(90)
while n > 0:
    t.forward(100)
    t.stamp()
    t.goto(0.00, 0.00)
    t.right(360/k)
    n -= 1