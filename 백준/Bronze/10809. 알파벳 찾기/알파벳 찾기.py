word = list(map(str, input()))

aList = [chr(i) for i in range(ord('a'), ord('z')+1)]

for x in aList:
    if x in word:
        print(word.index(x), end=' ')
    else:
        print(-1, end=' ')