import re
import string
frequency = {}
#частота
a = input("Введите фразу: ")
#входные данные
match_pattern = re.findall(r'\w+', a)
#сортирует слова
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
#счетчик
frequency_list = frequency.keys()
#ключ
for words in frequency_list:
    print (words, frequency[words])
#вывод