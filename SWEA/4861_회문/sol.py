import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T + 1):
    # N : 글자의 길이, 글자의 줄 수
    # M : 회문의 길이
    N, M = map(int, input().split())
    # N x N 크기의 격자
    data = [list(input()) for _ in range(N)]
    # 나 이때까지 input().split() 쓰고 있었음;;

    # 가로 단어
    for x in range(N):  # 행
        for y in range(N - M + 1):  # 열
            row_word = data[x][y:y+M]
            if row_word == row_word[::-1]:
                result = ''.join(row_word)
                print(f'#{test} {result}')
                break

    # 세로 단어
    for x in range(N - M + 1):  # 행
        for y in range(N):  # 열
            col_word = ''
            for i in range(M):
                word = data[i + x][y]
                col_word += word
            if col_word == col_word[::-1]:
                print(f'#{test} {col_word}')
                break