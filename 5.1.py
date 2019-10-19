def power(a1, n1):
    if not type(a1) == int:
        return False
    elif not type(n1) == int:
        return False
    elif a1 <= 0:
        return False
    elif n1 == 0:
        return 1
    elif a1 == 1:
        return 1
    else:
        b = 1
        for i in range(n1):
            b = b * a1
        return b


a = 1
n = 1
c = power(a, n)
if c == False:
    print('error')
else:
    print(c)
