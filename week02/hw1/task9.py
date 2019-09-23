def find_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)
    return distance

Xa = float(input())
Ya = float(input())
Xb = float(input())
Yb = float(input())
print(find_distance(Xa, Ya, Xb, Yb))