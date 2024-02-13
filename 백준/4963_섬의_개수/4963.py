import sys
sys.stdin = open('input.txt')

# 상하좌우/좌상,우상,우하,좌하
dt_x = [-1, 1, 0, 0, -1, -1, 1, 1]
dt_y = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        next_x = x + dt_x[i]
        next_y = y + dt_y[i]
        if 0 <= next_x < h and 0 <= next_y < w and land[next_x][next_y] == 1:
            if land[next_x][next_y] == 1 and visited[next_x][next_y] == 0:  # 방문 안 한 땅 있는 곳 있다면
                dfs(next_x, next_y)     # 재귀로 계속 탐색 이어나감

while True:
    cnt = 0
    # w: 너비, h: 높이
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 1은 땅, 0은 바다
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    for x in range(h):  # w 넣어서 계속 안 나옴;;;
        for y in range(w):
            if land[x][y] == 1 and visited[x][y] == 0:
                dfs(x, y)
                cnt += 1
    print(cnt)


