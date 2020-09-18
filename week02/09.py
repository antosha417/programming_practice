def distance(x1, y1, x2, y2):
    dist = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** (1 / 2)
    return dist


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
