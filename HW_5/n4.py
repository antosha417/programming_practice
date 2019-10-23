def diagonal(choice, n, matrix):
    total = 0
    if choice == 1:
        for i in range(n):
            total += matrix[i][i]
    else:
        for i in range(n):
            total += matrix[i][n - i - 1]
    return total


def main():
    t = 1
    while t:
        try:
            n = int(input("Введите натуральное число: "))
        except ValueError:
            print("Попробуйте еще раз")
        else:
            if n > 0:
                t = 0
            else:
                print("Попробуйте еще раз")
    matrix = []
    for i in range(n):
        t = 1
        while t:
            try:
                list_one = list(map(float, input("Введите числа для " + str(i + 1) + "-й строки: ").split()))
            except ValueError:
                print("Попробуйте еще раз")
            else:
                if len(list_one) == n:
                    t = 0
                else:
                    print("Попробуйте еще раз")
        matrix.append(list_one)
    print("Какую диагональ вы хотите посчитать?\n1. Главную\n2. Побочную")
    t = 1
    while t:
        try:
            num = int(input("Введите номер варианта: "))
        except ValueError:
            print("Попробуйте еще раз")
        else:
            if num in [1, 2]:
                t = 0
            else:
                print("Попробуйте еще раз")
    print(diagonal(num, n, matrix))
main()