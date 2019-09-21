distance = 109
speed = int(input())
time = int(input())
if speed > 0:
    print((speed * time) % distance)
else:
    print(distance - (abs(speed * time) % distance))
