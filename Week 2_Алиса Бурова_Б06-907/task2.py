#Напишете программу, которая на вход берет строку text и целое число n, и выводит в слово Hello, а также n раз через запятую и пробел строку text.
# В конце выхода запятая не ставится.
# Например, для text = MIPT Students и n = 5 результат будет следующим: Hello, MIPT Students, MIPT Students, MIPT Students, MIPT Students, MIPT Students
if __name__ == '__main__':
    line = input()
    n = int(input())
    arr = []
    arr.append(line)
    arr*=n
    arr.insert(0, "Hello")
    print(*arr, sep=", ")