def nod(list_of_nums):
    n1 = list_of_nums[0]
    n2 = list_of_nums[1]
    while n2 != n1:
        if n2 > n1:
            n2 -= n1
        else:
            n1 -= n2
    return n2

def main():
    t = 1
    while t:
        try:
            n = int(input("Введите количество пар: "))
        except ValueError:
            print("Попробуйте еще раз")
        else:
            t = 0
    list_of_nums = []
    t = 1
    print(n)
    for _ in range(n):
        while t:
            try:
                list_one = list(map(str, input("Введите пару чисел: ").split()))
                for i in range(len(list_one)):
                    list_one[i] = int(list_one[i])
            except ValueError:
                print("Попробуйте еще раз")
            else:
                if len(list_one) == 2:
                    t = 0
                    list_of_nums.append(list_one)
                else:
                    print("Попробуйте еще раз")
        t = 1
    print("{0:15}{1:20}{2}".format("Первое число","Второе число","НОД"))
    for i in range(n):
        print("{0:7}{1:15}{2:15}".format(list_of_nums[i][0], list_of_nums[i][1], nod(list_of_nums[i])))
main()