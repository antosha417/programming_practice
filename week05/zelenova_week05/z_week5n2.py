#2. Напишите функцию вычисляющие наибольшие общие делители (НОД) для множества пар чисел.
from z_week05n1 import checknum, checknumint

num = 0
ans=[]
def is_odd(number):
    return (number%2) !=0
def gcd(n,m):
        '''gcd = greatest common divider'''

        if m==0 or n==0:
            nod = (max(m,n))
        elif  n == m:
            nod = a
        elif  n == 1 or m == 1:
            nod = 1
        elif is_odd(n):
             if is_odd(m):
                 nod = gcd(n, abs(m-n))
             else:
                 nod = gcd(n, m/2)
        else:
             if is_odd(m):
                 nod = gcd(n/2, m)
             else:
                 nod = gcd(n/2, m/2)
        return nod

print('Сколько пар чисел, вы хотите ввести?')
a=checknumint(num)
dict={}
for i in range(a):
    print('введите',i+1,'пару чисел:')
    key=checknum(num)
    value=checknum(num)
    dict[key]=value

for i in dict:
        n=abs(i)
        m=abs(dict[i])
        ans.append(gcd(n,m))
for i in range(a):
        print('для пары',i+1,'НОД =',ans[i])

