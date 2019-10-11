def change_max_min(mas):
    mx=max(mas)
    mn=min(mas)
    for i in range(len(mas)):
        if mas[i]==mx:
            imax=i
        if mas[i]==mn:
            imin=i
    mas[imax],mas[imin]=mas[imin],mas[imax]
    for k in mas:
        print(k, end=' ')

arr=[int(s) for s in input().split()]
change_max_min(arr)