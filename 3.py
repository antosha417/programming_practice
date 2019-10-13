a = int(input())
b = int(input())
c = int(input())
if a<=c and a<=b:
    print(a)
elif b<=c and a>=b:
    print(b)
elif a>=c and c<=b:
    print(c)