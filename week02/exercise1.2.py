'''
Напишете программу, которая на вход берет строку text и целое число n, и выводит в слово Hello,
а также n раз через запятую и пробел строку text. В конце выхода запятая не ставится.
Например, для text = MIPT Students и n = 5 результат будет следующим:
 Hello, MIPT Students, MIPT Students, MIPT Students, MIPT Students, MIPT Students
'''
print ("Input the number")
n = input()
str0 = input()
n = int (n)
if n==1:
    print ('hello', str0)
else:
    #print ("hello" , (str0 + ', ' ) * (n-1) , str0)
    print("Hello "+(str0 + ', ')*(n-1)+str0)