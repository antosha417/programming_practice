from math import sin, pi

def s0(a):
    if  not (type(a) == int) or (type(a) == float):
        return False
    elif not a >= 0:
        return False
    else:
        s = pi * a * a
        return s

# площадь треугольника может быть < 0 если sin угла < 0
def s3(a, b, c:float = None, angle:float = None):
    if not ((type(a) == int) or (type(a) == float)):
        return False
    elif not ((type(b) == int) or (type(b) == float)):
        return False
    elif (c is None) and (angle is None):
        return 0.5*a*b
    elif (c is not None) and (angle is not None):
        return False
    elif (angle is None) and (not ((type(c) == int) or (type(c) == float))):
        return False
    elif (angle is None) and ((type(c) == int) or (type(c) == float)):
        if c < 0:
            return False
        else:
            return 0.25*(((a+b+c)*(a+b-c)*(a-b+c)*(b-a+c))**0.5)
    elif (c is None) and ((type(angle) == int) or (type(angle) == float)):
        return a*b*(sin(angle))
    else:
        return False

def s4(a,b):
    if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)):
        return a*b*0.5
    else:
        return False

def s(n:int = None, a:float = None, b:float = None, c:float = None, angle:float = None):
    if n == 0:
        return s0(a)
    elif n == 3:
        return s3(a, b, c, angle)
    elif n == 4:
        return s4(a, b)
    else:
        return False