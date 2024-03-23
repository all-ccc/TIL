dt_r = [0, 0, -1, 1]
dt_c = [-1, 1, 0, 0]

r, c = map(int, input().split())
data = [list(input()) for _ in range(r)]
after_50 = [['.'] * c for _ in range(r)]    # 50년 뒤의 땅

for row in range(r):    # 0 1 2 3 4
    for col in range(c):    # 0 1 2
        if data[row][col] == 'X':      # 땅일 때만 주변 탐색
            cnt = 0     # 주변 네 면 중 바다 카운트하는 변수
            for i in range(4):      # 상하좌우 탐색
                next_r = row + dt_r[i]
                next_c = col + dt_c[i]
                if 0 <= next_r < r and 0 <= next_c < c:     # 유효한 범위 내에 있다면
                    if data[next_r][next_c] == '.':     # 해당 부분이 바다인 경우
                        cnt += 1        # cnt + 1
                else:   # 범위 벗어나는 곳은 다 바다니까
                    cnt += 1
            if cnt < 3:
                after_50[row][col] = 'X'

s_row, e_row, s_col, e_col = r+1, -1, c+1, -1   # 시작 행, 마지막 행, 시작 열, 마지막 열
for i in range(r):
    for j in range(c):
        if after_50[i][j] == 'X':
            s_row = min(i, s_row)
            e_row = max(i, e_row)
            s_col = min(j, s_col)
            e_col = max(j, e_col)

for row in range(s_row, e_row+1):
    for col in range(s_col, e_col+1):
        print(after_50[row][col], end='')
    print()