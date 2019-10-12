n = int(input())
minutes = n % 60
hours = ((n - minutes) // 60) % 24
print(hours, minutes)