import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    # E : 간선의 개수
    t_case, E = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * 100
    stack = [0]
    result = 0

    # 인접 리스트
    adj_list = [[] for _ in range(100)]  # adj_list[i]행에 인접인 정점 번호

    for idx in range(0, E * 2, 2):  # 간선의 개수는 개당 2개의 노드번호 가짐
        from_node = arr[idx]
        to_node = arr[idx + 1]
        adj_list[from_node].append(to_node) # 방향 있으니까 하나만

    stack = [0]
    while stack:  # 조사 대상이 없어질 때까지
        now = stack.pop()  # LIFO
        if visited[now] == 0:
            visited[now] = 1  # 방문 표시
        # 다음번 조사 대상이 누구냐 -> 인접리스트 adj[now] 대상 모두 조사
        for next_v in adj_list[now]:
            if visited[next_v] == 0:  # 방문하지 않았다면
                stack.append(next_v)
    if visited[99] == 1:
        result = 1
    else:
        result = 0

    print(f'#{test} {result}')