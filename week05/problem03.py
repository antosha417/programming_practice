from math import pi


def square_of_triangle(a, h):
    return (1 / 2) * a * h


def square_of_rectangle(a, b):
    return a * b


def square_of_circle(a):
    return pi * (a ** 2)


def square_of_figure(name, a, b):
    if name == 'triangle':
        return square_of_triangle(a, b)

    elif name == 'rectangle':
        return square_of_rectangle(a, b)

    elif name == 'circle':
        return square_of_circle(a)

    else:
        return 'unavailable figure, please try again!!!!'


if __name__ == '__main__':
    name = input('name of figure from list(circle, triangle, rectangle): ')
    a1 = float(input(
        "length of the first parameter(radius for circle, length of side for others): "))  # первый параметр фигуры
    a2 = float(input(
        "length of the second parameter(extra for circle, height for triangle, length of side for rectangle): "))  # второй параметр фигуры
    print(square_of_figure(name, a1, a2))
