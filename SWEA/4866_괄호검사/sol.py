import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    top = -1
    bracket = input()
    stack = []
    # result = 1  # 실패하면 바로 break로 나가면 되나? 다시 생각
    # open_bracket = '({'
    # close_bracket = ')}' 머 이래 해가지고 in 써서
    for n in bracket:  # data를 하나씩 순회하면서
        if n == '(' or n == '{':   # 해당 문자가 '여는 괄호'라면
            top += 1
            stack.append(n)  # 해당 data를 넣어줌

        elif n == ')':  # 해당 문자가 '닫는 소괄호'라면
            if not stack: # stack 리스트가 비어있으면
                top += 1
                stack.append(n)
            elif stack and stack[top] == '(': # stack에 뭐가 있고 소괄호 짝이 맞을 경우
                top -= 1
                stack.pop()
            else:   # stack에 뭐가 있는데, 소괄호 짝이 안 맞을 경우
                top += 1
                stack.append(n)

        elif n == '}':  # 해당 문자가 '닫는 중괄호'라면
            if not stack:  # stack 리스트가 비어있으면
                top += 1
                stack.append(n)
            elif stack and stack[top] == '{':  # stack에 뭐가 있고 중괄호 짝이 맞을 경우
                top -= 1
                stack.pop()
            else:   # stack에 뭐가 있는데, 중괄호 짝이 안 맞을 경우
                top += 1
                stack.append(n)

    if stack:  # stack 리스트에 뭐가 남아있으면
        result = 0
    else:   # stack 리스트가 비어있으면
        result = 1
    # print(stack)

    print(f'#{test} {result}')

# 양심 있으면 다시 풀어라.............



# 강사님 풀이

# class Stack:
#     # stack을 생성할 때 필요한 값이 있는데,
#     # stack의 크기를 지정해야 한다.
#     def __init__(self, size):
#         self.size = size
#         # 자료구조 stack을 list를 활용해서 구현
#         self.data = [None] * size   # 값이 없음을 나타내는 None
#         self.top = -1   # 초기 값이 없으므로, top의 위치는 -1
#
#     def push(self, item):   # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받는다.
#         if self.is_full():  # stack이 가득 찼다면
#             print('Stack is Full!!')
#         else:
#             self.top += 1   # top 위치 1 증가
#             # 받아온 item을 내 data에 top번째 위치에 삽입한다.
#             self.data[self.top] = item
#
#     def get(self):  # top번째 있는 요소를 출력할 수 있는 방법
#         return self.data[self.top]
#
#     def __str__(self):  # instance print 했을 때, stack 안의 data를 바로 출력
#         return f'{self.data}'   # stack만 출력해도 data 나옴
#
#     def pop(self):
#         if self.is_empty(): # stack이 비었다면,
#             print('Stack is Empty!!')
#         else:
#             # top_value = self.data[self.top]   --> 굳이 이렇게 쓸 필요는 없음
#             # self.data[self.top] = None
#             self.top -= 1
#             # return top_value
#             return self.data[self.top + 1]  # 1 빼기 전의 위치 반환
#
#     def is_empty(self):
#         # top이 -1을 가리키고 있다면 stack은 비었다.
#         return self.top == -1
#
#     def is_full(self):
#         return self.size == self.top + 1
#
# T = int(input())
#
# for test in range(1, T+1):
#     bracket = input()
#     stack = Stack(100)
#     # 모든 문자열을 조사
#     result = 1
#     for char in bracket:
#         if char == '(': # 여는 괄호 나왔다면 stack에 추가해줌
#             stack.push(char)
#         elif char == ')':   # 닫는 괄호 나왔다면
#             if not stack.is_empty():    # stack이 비어있지 않은지 확인하고
#                 stack.pop() #
#             else:
#                 result = 0
#                 break
#
#     if not stack.is_empty():    # 조사가 다 끝남에도 stack이 비어있지 않다면
#         result = 0
#
#     print(f'#{test} {result}')