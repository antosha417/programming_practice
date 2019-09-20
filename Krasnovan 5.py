n = input()
x = 1
b = ''
a = ''
c = ')'
d = '0'
while x <= n:
    a = 'x*(1+'
    b = b + a
    x = x + 1
else:
    b = b + d
c = c * n
b = b + c
z = eval(b)
print(z)
