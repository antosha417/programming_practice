import math
def r(x1,y1,x2,y2):
    return (math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(r(x1,y1,x2,y2))