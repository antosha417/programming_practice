
def minutes_into_hours(x):
    hours_counter = (x//60) % 24
    minutes_counter = x % 60
    return hours_counter, minutes_counter

n = int(input())
hours, minutes = minutes_into_hours(n)
print(hours, minutes)
