def point(v,t):
    if v>0:
        print(v*t%109)
    else:
        print((109+v*t)%109)
v=int(input())
t=int(input())
point(v,t)