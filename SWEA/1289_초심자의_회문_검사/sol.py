import sys
sys.stdin = open('input.txt')

# 슬라이싱, for, while, 메서드와 빌트인함수 써서
# 4가지 함수 만들어서 풀어보기


T = int(input())

for test in range(1, T+1):
    result = 0
    word = input()
    if word == word[::-1]:
        result = 1
        print(f'#{test} {result}')
    else:
        print(f'#{test} {result}')
