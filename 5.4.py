def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sumM(a:list, choise:str = 'main'):
    if not type(a) == list:
        return False
    b = len(a[0])
    c = 0
    l = len(a)
    for i in range(l):
        if not len(a[i]) == b:
            c = 1
    if c == 1:
        return False
    a2 = ''
    for i in range(l):
        k = a[i]
        for ii in range (l):
            a2 = a2 + str(k[ii])
    if not isint(a2):
        return False
    else:
        if choise == 'main':
            mainsum = 0
            for i in range(l):
                m = a[i]
                mainsum += int(m[i])
            return mainsum
        elif choise == 'nomain':
            nomainsum = 0
            for i in range(l):
                m = a[i]
                nomainsum += int(m[-i-1])
            return nomainsum
        else:
            return False

a = [[1, 2, 3], [3, 4, 5], [0, 0, 0]]
print(sumM(a, 'nomain'))
