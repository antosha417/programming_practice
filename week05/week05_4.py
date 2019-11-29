"""Напишите функцию, которая на вход принимает квадратную матрицу (например, в виде списка списков).
Вычисляет сумму элементов главной или побочной диагонали в зависимости от выбора пользователя.
Сумма элементов любой диагонали должна вычисляться в одной и той же отдельной функции"""

# первая строка ввода - это количество строк массива
def main():
    n = int(input("Dimension of matrix: "))
    print("Enter matrix: ")
    a = []
    for i in range(n):
        row = input().split()
        for i in range(n):
            row[i] = int(row[i])
        a.append(row)
    traceq = input("main trace/side trace: ")
    if traceq == 'main trace':
        trace(0, 1, n, a)
    if traceq == 'side trace':
        trace(n - 1, -1, n, a)




def trace(k, p, n, a):
    sum = 0
    for t in range(n):
        sum += a[k + p * t][t]
    print(sum)

if __name__== "__main__":
    main()