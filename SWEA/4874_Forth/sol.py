import sys
# sys.stdin = open('input.txt')

T = int(input())
stack = [0] * 256
temp = ''

for test in range(1, T+1):
    code = input().split()
    stack = []
    result = 'error'

    for token in code:
        if token.isdecimal():   # 숫자일 경우 stack에 추가
            stack.append(int(token))
        elif token in '*/+-' and len(stack) >= 2:   # 연산자이고 stack 길이가 2 이상일 경우 연산 수행
            b = stack.pop()
            a = stack.pop()
            if token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
            elif token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
        elif token == '.' and len(stack) == 1:  # .이고 stack 길이가 1일 경우 stack에서 pop을 해서 결과 출력
            result = stack.pop()
        else:   # 위에 해당되지 않는 경우는 모두 error로 처리 후 반복문 빠져나옴
            break

    print(f'#{test} {result}')