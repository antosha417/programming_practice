def where_is_Vasya(speed, hours):
    if speed > 0:
        distance = (speed * hours) % 109
    return distance

v = int(input())
t = int(input())
vasyas_location = where_is_Vasya(v, t)
print(vasyas_location)

#я понимаю, что можно было в три строчки решить, но мне очень нравится составлять функции:)
