def NOD(a: int, b: int):
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(NOD(a, b))
