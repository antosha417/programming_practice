def sum_of_main(l: list):
    ans1 = 0
    for i in range(len(l)):
        ans1 += l[i][i]
    return ans1


def sum_of_secondary(l: list):
    ans2 = 0
    for i in range(len(l)):
        ans2 += l[i][len(l) - i - 1]
    return ans2


def sum_of_diagonal(name: str, lst: list):
    if name == "main":
        return sum_of_main(lst)
    elif name == "secondary":
        return sum_of_secondary(lst)
    else:
        return "Please type correct name!!!!!"


if __name__ == '__main__':
    # Example of working
    from random import random  # creating of array

    n = 4
    matrix = []
    for i in range(n):
        lst = []
        for j in range(n):
            lst.append(int(random() * 10))
        matrix.append(lst)
    name = input('choose type of diagonal: ')
    print(matrix, 'answer: ', sum_of_diagonal(name, matrix))
