def nod(n1, n2):
    if n1 == 0:
        return False
    elif n2 == 0:
        return False
    else:
        while n1 != 0 and n2 != 0:
            if n1 > n2:
                n1 %= n2
            else:
                n2 %= n1
        return n1 + n2

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def NOD(a):
    if not type(a) == list:
        return False
    if a == []:
        return False
    t = True
    for i in range(len(a1)):
        if not type(a[i]) == list:
            t = False
    if t == False:
            return False
    t = True
    for i in range (len(a1)):
        if not len(a[i]) == 2:
            return False
    t = True
    for i in range (len(a1)):
        b = a[i]
        if isint(b[0]) == False:
            t = False
        if isint(b[1]) == False :
            t = False
    if t == False:
        return False
    else:
        t = True
        d = []
        for i in range (len(a1)):
           b = a[i]
           c1 = int(b[0])
           c2 = int(b[1])
           d.append(nod(c1, c2))
           if nod(c1, c2) == False:
               t = False
        if t == False:
            return False
        else:
            return d

a1 = [[1, 3], [2, 3], [4, 6], [24, 6], [12, 9]]
print(NOD(a1))