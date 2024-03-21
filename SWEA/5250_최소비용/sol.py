import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush
# heap의 특성을 좀 알아라~~~!!!!

def prim(x, y):     # 시작하는 곳 좌표
    pq = []
    sum_weight = 0
    visited = [[0] * N for _ in range(N)]
    heappush(pq, (x, y))
    while pq:
        now_x, now_y = heappop(pq)
        now_h = data[now_x][now_y]  # 현재 좌표의 높이
        for i in range(4):
            next_x = x + dt_x[i]
            next_y = y + dt_y[i]
            if 0 <= next_x < N and 0 <= next_y < N:   # 유효한 범위 내에 있는 경우
                if visited[next_x][next_y] == 1:    # 이미 방문했다면 continue
                    continue
                else:   # 아직 방문 안 한 곳이라면
                    # height 비교 (if data[x][y]와 같거나 아님 젤 차이 작은 거)
                    if data[next_x][next_y] == now_h:
                        visited[next_x][next_y] = 1
                        heappush(pq, (next_x, next_y))
                        break
                    elif data[next_x][next_y] > now_h:
                        visited[next_x][next_y] = 1
                        heappush(pq, (next_x, next_y))

                # heappush 하고 나서 sum_weight 올려줘
                # 다음이 도착지인 경우


# 우, 하 방향만.. 할랬는데 모르겠다 최소한의 연료니까
dt_x = [0, 0, -1, 1]
dt_y = [-1, 1, 0, 0]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    prim(0, 0)