def f(x):
    y = 0
    if x < -5:
        y = (-2)*x - 1
    elif x > 5:
        y = 2*x
    else:
        y = x**2
    return y


import matplotlib.pyplot as plt
A = []
B=[]
for i in range(21):
    A.append(i-10)
for elem in A:
    B.append(f(elem))
plt.plot(A,B)
plt.show()