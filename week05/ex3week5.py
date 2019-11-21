import math
def square_triangle(side1, side2, side3):
    half_perimeter = (side1 + side2 + side3)/2
    end_value = (half_perimeter*(half_perimeter - side1)*(half_perimeter - side2)*(half_perimeter - side3))**0.5
    if isinstance(end_value, complex) == False:
        return end_value
    else:
        print("The specified triangle does not exist")
def square_circle(r):
    return math.pi*r*r
def square_rectangle(length, width):
    return length*width
print("""For which figure do you want to calculate the square?
1.triangle 
2.circle
3.rectangle""")
my_figure = int(input())
if my_figure == 1:
    side1 = float(input("lenght of the first side: "))
    side2 = float(input("lenght of the second side: "))
    side3 = float(input("lenght of the third side: "))
    print(square_triangle(side1, side2, side3))
elif my_figure == 2:
    radius = float(input("lenght of circle`s radius: "))
    print(square_circle(radius))
elif my_figure == 3:
    lenght = float(input("rectangle`s lenght: "))
    width = float(input("rectangle`s width: "))
    print(square_rectangle(lenght, width))
else:
    print('This figure is not processed')