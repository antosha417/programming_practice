def gcd(a,b):
    if b == 0:
        return(a)
    else:
        return(gcd(b, a % b))

print("Enter the amount of pairs of numbers")
n = int(input())
print("Choose the way you want to receive answer:")
print("1. After every pair I've entered")
print("2. After all pairs I've entered")
print("Enter the number of the way you've chosen")
way = int(input())
if way == 1:
    for i in range(n):
        a, b = map(int,input().split())
        print(gcd(a,b))
elif way == 2:
    pairs_gcd = []
    for i in range(n):
        a, b = map(int, input().split())
        pairs_gcd.append(gcd(a,b))
    print(pairs_gcd)
else:
    print("Wrong input, please try again")