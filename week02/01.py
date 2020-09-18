n = int(input())
ch = n // 60
min = n % 60
if ch >= 24:
    ch = ch % 24
print(ch, min)
