v = int(input())
t = int(input())
if v >= 0:
    s = (v * t) % 109
else:
    s = (109 + v * t) % 109
print(s)