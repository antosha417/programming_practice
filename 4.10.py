namelist = []
listpokupok = []
goodslist = []
a = []
d = 0
sortlist = []
while 0 == 0:
    s = input()
    if s == 'end':
        break
    b = s.split(' ')
    a = a + b
l1 = len(a)
for i in range(0, l1, 3):
    namelist.append(a[i])
namelist = list(set(namelist))
namelist.sort()
# namelist [покупатель1, покупатель2 ...]
# listpokupok [товар1, число, товар2, число...]
# goodslist [товар1, товар2 ...]
# sortlist [товар1, число, товар2, число...] товары не повторяются
l2 = len(namelist)
for i in range (0, l2):
    for ii in range (0, l1, 3):
        if namelist[i] == a[ii]:
            listpokupok.append(a[ii+1])
            listpokupok.append(a[ii+2])
    l3 = len(listpokupok)
    for iii in range (0, l3, 2):
        goodslist.append(listpokupok[iii])
    goodslist = list(set(goodslist))
    goodslist.sort()
    l4 = len(goodslist)
    for iiii in range (0, l4):
        for iiiii in range (0, l3, 2):
            if goodslist[iiii] == listpokupok[iiiii]:
                d += int(listpokupok[iiiii+1])
        sortlist.append(goodslist[iiii])
        sortlist.append(d)
        d = 0
    listpokupok = []
    goodslist = []
    d = 0
    print(namelist[i], sortlist)
    sortlist = []
