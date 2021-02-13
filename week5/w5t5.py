import matplotlib.pyplot as plt

def f (x):
    if x < -5:
        return(2 * abs(x) - 1)
    elif x > 5:
        return(2 * x)
    else:
        return(x ** 2)

x, y = [], []
for i in range(21):
    x.append(i - 10)
for elem in x:
    y.append(f(elem))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha = 0.5)
plt.show()