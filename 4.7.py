a = []
s0 = input()
f = int(s0)
for i in range (0, f):
    s = input()
    b = s.split()
    a = a + b
a = list(set(a))
t = len(a)
print(t)
