import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T + 1):
    # N : 글자의 길이, 글자의 줄 수
    # M : 회문의 길이
    N, M = map(int, input().split()) # 20 13 -> 8번을 돌아야
    # N x N 크기의 격자
    data = [list(input().split()) for _ in range(N)]

    # 가로 단어
    for x in range(N):  # 행
        for y in range(N-M+1):  # 열
            row_word = data[x][0][y:y+M]
            print(row_word)
            if row_word == row_word[::-1]:
                print(f'#{test} {row_word}')
                break

    # 세로 단어
    col_word = ''
    for x in range(N):  # 행
        for y in range(N-M+1):  # 열
            for i in range(M):
                word = data[i+y][x] # out of range
                print(word)
            #     col_word += word
            #     print(col_word)
            # if col_word == col_word[::-1]:
            #     print(f'#{test} {col_word}')
            #     break
    # 다시 풀기 ㅎ;
