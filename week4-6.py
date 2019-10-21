string = str(input())
spisok = list(string)
c = set()
print(spisok)
while spisok.count(' ') != 0:
    spisok.remove(' ')
for i in range(len(spisok)):
    if spisok[i] in c:
        print('yes')
    else:
        c.add(spisok[i])
        print('no')
print(c)
print(spisok)
