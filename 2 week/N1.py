"""min -> hours + min"""

n = int(input())
hours = (n//60)%24
minuts = n - (n//60)*60
print (hours, "hours", minuts, "min")