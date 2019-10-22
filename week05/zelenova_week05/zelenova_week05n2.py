#2. Напишите функцию вычисляющие наибольшие общие делители (НОД) для множества пар чисел.

print('Сколько пар чисел, вы хотите ввести?')
a=int(input())
dict={}
for i in range(a):
    print('введите',i+1,'пару чисел:')
    key=int(input())
    value=int(input())
    dict[key]=value
def gcd(dict):
    '''gcd = greatest common divider for every pair from dictionary(dict). creates list nod with the answers'''
    nod=[]
    for i in dict:
        n=abs(i)
        m=abs(dict[i])
        if m==0 or n==0:
            nod.append(max(m,n))
        for i in range(min(m,n)):
            if n%(min(m,n)-i)==0 and m%(min(m,n)-i)==0:
                nod.append(min(m,n)-i)
                break
    return nod
gcd(dict)
for i in range(a):
    print('для пары',i+1,'НОД =',gcd(dict)[i])

