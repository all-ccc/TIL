word = input().upper()
word_set = list(set(word))
count_list = []

for i in word_set:
    count_list.append(word.count(i))

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(word_set[count_list.index(max(count_list))])