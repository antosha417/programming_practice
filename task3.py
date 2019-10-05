#Даны три целых числа. Выведите значение наименьшего из них.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)