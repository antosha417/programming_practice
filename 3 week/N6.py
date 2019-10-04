import turtle as t
t.shape('turtle')
n = 10
R = 50
fi = 360/n
for i in range(1, n+1):
    t.forward(R)
    t.stamp()
    t.backward(R)
    t.right(fi)
