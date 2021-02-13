print("Enter the amount of strings in your matrix")
n = int(input())
print("Enter your matrix line by line")
matrix = []
for i in range(n):
    matrix.append(input().split())
print("Enter the type of the diagonal you want to calculate")
diagonal = input()
summ = 0
if diagonal == 'main' or diagonal == "Main":
    for i in range(n):
        summ += int(matrix[i][i])
    print(summ)
elif diagonal == 'side' or diagonal == "Side":
    for i in range(n):
        summ += int(matrix[i][n - i])
    print(summ)
else:
    print("Wrong input, please try again")