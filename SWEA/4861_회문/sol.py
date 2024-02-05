import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T + 1):
    # N : 글자의 길이, 글자의 줄 수
    # M : 회문의 길이
    N, M = map(int, input().split())
    result = ''
    # N x N 크기의 격자?
    word_list = [list(input().split()) for _ in range(N)]

    for x in range(N-M):
        for y in range(N-M):
            result_1 = str(word_list[x:x+M+1][y])   # 가로 단어
            result_2 = str(word_list[x][y:y+M+1])   # 세로 단어
            if result == result[::-1]:
                print(result)
            else:
                continue
    # print(f'#{test} {result}')





