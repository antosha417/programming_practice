def gcd(a, b):
    d_max = 1
    if a < b:
        for i in range(1, a+1):
            if (a%i == 0) and (b%i == 0):
                if i > d_max:
                    d_max = i
    else:
        for i in range(1, b+1):
            if (a%i == 0) and (b%i == 0):
                if i > d_max:
                    d_max = i
    return d_max


print("Write the number of pairs:")
n = int(input())
for i in range(n):
    a_i, b_i = map(int, input().split())
    print(gcd(a_i, b_i))