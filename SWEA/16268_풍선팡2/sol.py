import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    N, M = map(int, input().split())
    # N : 행의 수 3
    # M : 열의 수 5

    # 종이 꽃가루 개수 들어간 2차원 리스트
    data = [list(map(int, input().split())) for _ in range(N)]

    #           상  하  좌  우
    delta_row = [-1, 1, 0, 0]
    delta_col = [0, 0, -1, 1]

    # N x M 의 위치 하나하나를 돌면서 터지는 꽃가루 수 계산(flower)해서 list에 저장
    flower_lst = []
    for x in range(N): # 0 1 2
        for y in range(M): # 0 1 2 3 4
            # 방향 당 터지는 꽃가루 수 += 로 더해줌
            # 처음엔 현재 위치의 꽃가루 값
            flower = data[x][y]
            for i in range(4): # 상하좌우 네 가지 방향
                # 방향 별 x, y 좌표 값
                next_row = x + delta_row[i]
                next_col = y + delta_col[i]
                # next 좌표가 data 안에 위치
                if 0 > next_row or next_row > N:
                    flower += data[next_row][next_col]
                else:   # data 안에 위치하지 않을 때
                    continue
                # out of range 뜨는데 data 안에 위치하지 않을 때를 조건 첫번째로 해야 하는지

            flower_lst.append(flower)

    print(f'{test} {max(flower_lst)}')
