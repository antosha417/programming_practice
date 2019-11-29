def gcd2(m, n):
    if m % n != 0:
        return gcd2(n, m % n)
    else:
        return n

def main():
    n = int(input('How many pairs: '))
    a = []
    for i in range(n):
        row = input().split()
        for i in range(2):
            row[i] = int(row[i])
        a.append(row)

    for i in range(n):
        print(gcd2(a[i][0], a[i][1]))
main()