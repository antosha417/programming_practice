min = int(input())
if min > 1439:
    alfa = min // 1440
    min = min - alfa * 1440

if min < 60:
    print(0, ' ', min)

if min > 60:
    hour = min // 60
    min = min - hour * 60
    print(hour, ' ', min)
