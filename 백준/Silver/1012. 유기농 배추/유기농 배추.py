import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(r, c):
    for i in range(4):
        next_r = r + dt_r[i]
        next_c = c + dt_c[i]
        if 0 <= next_r < row and 0 <= next_c < col and field[next_r][next_c] == 1:  # 유효한 범위 내에 위치하고, 배추가 있는 곳이라면
            field[next_r][next_c] = 0   # 방문 표시
            dfs(next_r, next_c)

dt_r = [0, 0, -1, 1]
dt_c = [-1, 1, 0, 0]

T = int(input())
for _ in range(T):
    col, row, K = map(int, input().split())
    field = [[0] * col for _ in range(row)]     # 밭 모든 곳 0으로 초기화
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1     # x, y 값을 받아서 배추가 있는 곳은 1로 변경

    for i in range(row):
        for j in range(col):
            if field[i][j] == 1:    # 배추가 있는 곳이라면 dfs 실행
                field[i][j] = 0     # 방문 처리를 이렇게
                dfs(i, j)
                cnt += 1        # dfs 한 번 완료할 때마다 cnt 올려주기
    print(cnt)