import sys
# sys.stdin = open('input.txt')

def bfs(x1, y1):  # 시작 좌표, 도착 좌표
    q = []                      # 큐 생성
    visited = [[0] * N for _ in range(N)]       # visited 생성
    q.append([x1, y1])                 # 시작점 인큐 (여기에 좌표를 넘겨줘야
    visited[x1][y1] = 1              # 시작점 방문 표시
    while q:                    # 처리 안된 정점이 남아있으면
        t = q.pop(0)    # 처리할 좌표
        for i in range(4):           # 4가지 방향에 대해서
            next_x = t[0] + dt_x[i]
            next_y = t[1] + dt_y[i]
            if (0 <= next_x < N and 0 <= next_y < N) and data[next_x][next_y] != 1:   # 통로라면
                if visited[next_x][next_y] == 0:  # 방문하지 않았으면
                    q.append([next_x, next_y])         # 인큐하고
                    visited[next_x][next_y] = 1 + visited[t[0]][t[1]]     # 방문표시
                    if data[next_x][next_y] == 3:
                        return visited[t[0]][t[1]] - 1
            else:
                continue      # 벽이라면 다음 반복문으로
    return 0        # G까지 경로가 없는 경우



# 상하좌우
dt_x = [0, 0, -1, 1]
dt_y = [-1, 1, 0, 0]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    s_x, s_y = 0, 0
    e_x, e_y = 0, 0
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                s_x, s_y = x, y     # 출발 좌표

    result = bfs(s_x, s_y)
    print(f'#{test} {result}')
    # 0은 통로, 1은 벽, 2는 출발, 3은 도착
