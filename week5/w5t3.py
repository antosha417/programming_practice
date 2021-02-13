import math

def circle(r):
    return math.pi * r * r

def triangle(*, height = None, side1 = None, side2 = None, side3 = None, angle = None):
    if height == None:
        if angle == None:
            p = 0.5 * (side1 + side2 + side3)
            return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
        else:
            return side1 * side2 * 0.5 * math.sin(angle * math.pi / 180)
    else:
        return 0.5 * side1 * height
def rectangle(*, side1 = None, side2 = None, d1 = None, d2 = None, angle = None):
    if angle == None:
        return side1 * side2
    else:
        return d1 * d2 * 0.5 * math.sin(angle * math.pi / 180)
print("Enter the shape type:")
shape = str(input())
if shape == 'circle' or shape == 'Circle':
    print('Enter the radius')
    r = int(input())
    print(circle(r))
elif shape == 'triangle' or shape == 'Triangle':
    print("Choose the way you want to calculate the area:")
    print("1. Side and its height")
    print("2. Two sides and angle between them")
    print("3. Three sides")
    print("Enter the number of the way you've chosen")
    way = int(input())
    if way == 1:
        print( "Enter side and its height")
        side, height = map(int, input().split())
        print(triangle(side1 = side, height = height))
    elif way == 2:
        print("Enter two sides and angle between them")
        side1, side2, angle = map(int, input().split())
        print(triangle(side1 = side1, side2 = side2, angle = angle))
    elif way == 3:
        print("Enter three sides")
        side1, side2, side3 = map(int, input().split())
        print(triangle(side1 =side1, side2 = side2, side3 = side3))
    else:
        print("Wrong input, please try again")
elif shape == 'rectangle' or shape == 'Rectangle':
    print("Choose the way you want to calculate the area:")
    print("1. Two sides")
    print("2. Two diagonals and angle between them")
    print("Enter the number of the way you've chosen")
    way = int(input())
    if way == 1:
        print("Enter two sides")
        side1, side2 = map(int, input().split())
        print(rectangle(side1 = side1, side2 = side2))
    elif way == 2:
        print("Enter two diagonals and angle between them")
        d1, d2, angle = map(int, input().split())
        print(rectangle(d1 = d1, d2 = d2, angle = angle))
else:
    print('Wrong type, please try again')