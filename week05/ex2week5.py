def gcf(a:int, b:int):
    result = 1
    if a > 0 and b > 0:
        for i in range(1, a + 1):
            if b % i == 0:
                if a % i == 0:
                      result = i
    else:
        result = 'Not acceptable values'
    return result

print("""How do you want to get result?
1. After each pair of numbers
2. After all numbers""")
way = int(input())
if way == 1:
    amount_pairs = int(input('Amount of pairs: '))
    for i in range(amount_pairs):
        a, b = [int(s) for s in input().split()]
        print(gcf(a, b))
if way == 2:
    my_list = [int(s) for s in input().split()]
    if len(my_list) % 2 == 0:
        for i in range(0, len(my_list), 2):
            print(gcf(my_list[i], my_list[i + 1]))
    else:
        print("Amount of numbers must be evenly")
else:
    print("This value is not valid")




