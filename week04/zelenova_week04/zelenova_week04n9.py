#9.	Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# (pythontutor.ru, занятие 11, «Самое частое слово»)

n=int(input())
words=[]
oftwords=set()
for k in range(n):
     words+=(input().split())

dict={}
for i in range (len(words)):
    if words[i] not in dict:
            dict[words[i]] = 1
    else:
            dict[words[i]] += 1
m=max(list(dict.values()))
for i in dict:
    if dict[i]==m:
        oftwords.add(i)
print(min(oftwords))

