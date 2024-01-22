original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5' # 제거할 대상
arr = []

word_list = list(map(str, original_word))
arr.extend(word_list)
print(arr)

def restructure_word(word, arr):
    for str in word:
        if str.isdecimal():
            for i in range(int(str)):
                arr.pop()
        else:
            arr.remove(str)
    return arr


result = restructure_word(word, arr)
print(result)

print(''.join(result))
