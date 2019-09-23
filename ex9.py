x1 = float(input("Координата первой точки по оси абцисс: "))
x2 = float(input("Координата второй точки по оси абцисс: "))
y1 = float(input("Координата первой точки по оси ординат: "))
y2 = float(input("Координата второй точки по оси ординат: "))
def distance(x1, x2, y1, y2):
    result = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(result)
distance(x1, x2, y1, y2)

