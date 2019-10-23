def power(a,n):
    a1 = 1
    if n != 0:
        if n < 0:
            n = abs(n)
            a = 1 / a
        for _ in range(n):
            a1 *= a
    return a1

def main():
    t = 1
    while t:
        try:
            a = float(input("Введите действительное положительное число: "))
        except ValueError:
            print("Попробуйте еще раз")
        else:
            if a > 0:
                t = 0
            else:
                print("Попробуйте еще раз")
    t = 1
    while t:
        try:
            n = int(input("Введите целое число: "))
        except ValueError:
            print("Попробуйте еще раз")
        else:
            t = 0
    print(power(a,n))
main()