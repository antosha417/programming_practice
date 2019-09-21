v = int(input())
t = int(input())
s = abs(v)*t%109

if v<0 and s!=0:
    print (109-s)
elif s!=0:
    print (s)
else:
    print(0)
