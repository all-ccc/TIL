import sys
# sys.stdin = open('input.txt')

def bfs(s, N, G):  # 시작정점 s, 노드 개수 N, 도착 노드 G
    q = []                      # 큐 생성
    visited = [0] * (N+1)       # visited 생성
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 방문 표시
    while q:                    # 처리 안된 정점이 남아있으면
        t = q.pop(0)    # 처리할 정점 디큐
        if t == G:
            return visited[t] - 1   # 최단 경로 간선 수
        for i in adjl[t]:            # t에 인접인 정점 i
            if visited[i] == 0:     # 인큐되지 않았으면(처리된 적이 없으면)
                q.append(i)         # 인큐하고
                visited[i] = 1 + visited[t]     # 방문표시
    return 0        # G까지 경로가 없는 경우

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 리스트
    adjl = [[] for _ in range(V+1)]     # 0번부터 V번 까지의 행을 갖는 인접 리스트
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)     # 무향 그래프
    S, G = map(int, input().split())

    print(f'#{test} {bfs(S, V, G)}')
