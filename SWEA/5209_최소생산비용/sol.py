import sys
sys.stdin = open('input.txt')

def backtracking(row, sum_now):
    global min_cost
    if sum_now >= min_cost:     # 이때까지의 합이 min보다 크면
        return      # 볼 필요도 읎다

    elif row == N:      # 행 끝까지 간 경우
        min_cost = sum_now

    else:
        for i in range(N):
            if not col_visited[i]:  # 아직 방문 안 한 열이면
                col_visited[i] = 1  # 방문 처리해주고
                backtracking(row + 1, sum_now + cost_lst[row][i])
                col_visited[i] = 0


T = int(input())
for test in range(1, T+1):
    N = int(input())
    cost_lst = [list(map(int, input().split())) for _ in range(N)]  # 공장별 생산비용
    min_cost = 100 * N
    col_visited = [0] * N
    backtracking(0, 0)

    print(f'#{test} {min_cost}')