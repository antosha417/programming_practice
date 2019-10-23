def power(a:float, n:int):
    value = 1
    if a > 0 and isinstance(n, int) and n > 0:
        for i in range(n):
            value *= a
        return value
    else:
        print('Not acceptable')


print(power(float(input("Число, которое будет возводится: ")), int(input("Степень возведения: ", ))))


