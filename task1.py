n =int(input())
a = n//60
b = n - a*60
if a>24: a = a%24
print(a,"hrs", b,"mins")