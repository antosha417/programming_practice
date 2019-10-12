v, t = map(int, input().split())
if v > 0:
    print((v * t) % 109)
else:
    print(109 - (abs(v) * t) % 109)