def distance(a, b, c, d):
    dist = ((a - b)**2 + (c - d)**2)**0.5
    print(dist)


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
distance(x1, x2, y1, y2)