from math import pi

def square_circle(R,):
    return pi*R**2

def square_trianlge(a,h):
    return a*h/2

def square_rectangle(a,b):
    return a*b

st=input()
if st=='circle':
    print('Enter the radius')
    r=int(input())
    print(square_circle(r))
elif st=='triangle':
    print('Enter the length of one side and the height to it')
    a=int(input())
    h=int(input())
    print(square_trianlge(a,h))
elif st=='rectangle':
    print('Enter two adjacent sides')
    a=int(input())
    b=int(input())
    print(square_rectangle(a,b))