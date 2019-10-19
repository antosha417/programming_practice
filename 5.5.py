import matplotlib.pyplot as plt

def y(x):
    if not type(x) == int:
        return False
    elif (-5 <= x) and (x <= 5):
        return x * x
    elif x < -5:
        return - (2 * x) - 1
    elif x > 5:
        return 2 * x
    else:
        return False

X = []
Y = []
for i in range (-10, 10):
    X.append(i)
    Y.append(y(i))
linee = plt.plot(X, Y, 'bD:')
plt.axis([-10, 15, 0, 30])
plt.title(u'function')
plt.xlabel(u'x')
plt.ylabel(u'y')
plt.grid()
plt.savefig('functionn.png', format = 'png')