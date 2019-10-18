def uniquenum(s: str):
    lst = s.split()
    print("NO")
    for i in range(1, len(lst)):
        itr = 0
        for j in range(i):
            if lst[i] == lst[j]:
                print('YES')
                break
            else:
                itr += 1
                if itr == i:
                    print('NO')
    return " "


n = input()
print(uniquenum(n))
