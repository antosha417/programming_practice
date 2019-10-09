a = []
text = input()
text = text.split(' ')
a = list(set(text))
l = len(a)
m = len(text)
b = 0
for i in range (0, l):
    for ii in range (0, m):
        if a[i] == text[ii]:
            b += 1
    print(a[i], b)
    b = 0