from math import *

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    list0 = list(map(float, input().split()))
    print(distance(list0[0], list0[1], list0[2], list0[3]))
main()