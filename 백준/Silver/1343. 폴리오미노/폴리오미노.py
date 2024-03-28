str = input().split('.')    # 문자로만 이루어진 리스트
# print(str)
result = ''
for x in str:
    if len(x) % 2 == 1 and x != '.':
        print(-1)
        break
    while len(x) >= 4:
        result += 'AAAA'
        x = x[4:]
    if len(x) == 2:
        result += 'BB'
        x = x[2:]
    if x == '':
        result += '.'
else:
    print(result[:-1])  # 마지막에 .이 출력되는 거 막기 위해서...