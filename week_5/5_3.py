def triangle(a,h):
    s=(a*h)/2
    return s


def rectangle(a,b):
    s=a*b
    return s


def circle(r):
    import math
    s = math.pi * (r**2)
    return s


print("Choose the shape:")
shape=input()
if shape=="triangle":
    print("Enter the side and the height:")
    a0, h0 = map(int, input().split())
    print(triangle(a0, h0))
elif shape == "rectangle":
    print("Enter 2 sides:")
    a1, b1 = map(int, input().split())
    print(rectangle(a1,b1))
elif shape == "circle":
    print("Enter the radius:")
    r0=int(input())
    print(circle(r0))
else:
    print("Wrong type, try again.")