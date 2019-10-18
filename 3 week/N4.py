import turtle as t
R = 500
n = 90
fi = 360/n
for i in range(0, n):
    t.forward(R//n)
    t.left(fi)

"""
тоже, но долго
for i in range(200):
    t.forward(1)
    t.left(3)
"""