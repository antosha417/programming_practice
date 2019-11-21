import re
amount_str = int(input())
my_text = ''
for i in range(amount_str):
    string = input()
    my_text += string
my_text_words = re.sub(r'[,.;:]', ' ', my_text)
my_text_words_useful = set(re.split(r' ', my_text_words))
print(len(my_text_words_useful)-1)
