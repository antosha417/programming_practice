m1 = 0
m2 = 0
a = 1
while not a == 0:
    a = int(input())
    if a > m2:
        if a >= m1:
            m2 = m1
            m1 = a
        else:
            m2 = a
print(m2)