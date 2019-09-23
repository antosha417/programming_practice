def find_min(a, b, c):
    min = a
    if a > b:
        min = b
        if b > c:
            min = c
    elif a > c:
        min = c
    return min

x1 = int(input())
x2 = int(input())
x3 = int(input())
minimum = find_min(x1, x2, x3)
print(minimum)