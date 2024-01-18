one = 3
two = 0
print(one or two) # 3 (단축평가)
                  # 뒤에까지 평가할 필요 없이 one에서 만족했으니까 3 출력
if one or two:  # if 3:
    print('or 연산 통과')
else:
    print('or 연산 통과 못함')

print(0 == False)
print(-1 == True)

if '':
    print('빈 문자열은... 빈 문자열?')
else:
    print('아무 일도 벌어지지 않음')

three = ''
four = '4'
print(three and four)
if three and four: # if ''
    print('3과 4')
else:
    print('실패')


if one % 2:
    print('홀수')

if one % 2 == 1:
    print('홀수')
else:
    print('짝수')