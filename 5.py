p = int(input())
a = 1
su = 0
for i in range (1, p+1, 1):
    a*=i
    su+=a
print(su)