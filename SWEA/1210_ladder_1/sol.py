import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # ladder = [[0] * 100] * 100 -> 이렇게 하면 복제돼서 숫자 하나 바꾸면 다 바뀜

    end_col = ladder[99].index(2) # 마지막 행에서 2가 있는 열을 찾아서 end_col에 5
    end_row = 95

    while end_row != 0:
        # 좌우 중 1이 있으면 그쪽 열로 옮김
        # 지나간 곳 0으로 해서 지나온 곳 다시 안 가도록
        if 0 < end_col <= 99 and ladder[end_row][end_col - 1] == 1:
            ladder[end_row][end_col] = 0
            end_col -= 1
        elif 0 <= end_col < 99 and ladder[end_row][end_col + 1] == 1:
            ladder[end_row][end_col] = 0
            end_col += 1
        # 없으면 row -= 1 -> 위로 이동
        elif ladder[end_row - 1][end_col] == 1:
            end_row -= 1
            if end_row == 0:
                print(f'#{test} {end_col}')