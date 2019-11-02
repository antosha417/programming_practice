minimum = int(input())
if minimum > 1439:
    alfa = minimum // 1440
    minimum = minimum - alfa * 1440

if minimum < 60:
    print(0, ' ', minimum)

if minimum >= 60:
    hour = minimum // 60
    minimum = minimum - hour * 60
    print(hour, ' ', minimum)
