word = list(map(str, input()))

# aList = [chr(i) for i in range(ord('a'), ord('z')+1)]
# 아래와 똑같은 결과 나옴

aList = []
for i in range(ord('a'), ord('z')+1):
    aList.append(chr(i))
print(aList)

for x in aList:
    if x in word:
        print(word.index(x), end=' ')
    else:
        print(-1, end=' ')