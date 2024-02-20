# import sys
# sys.stdin = open('input.txt')


def solution(k):
    print(tree[k][0], end='')


def in_order(now):
    if now != 0:
        in_order(tree[now][1])
        solution(now)
        in_order(tree[now][2])


for test in range(1, 11):
    V = int(input())        # 노드 개수
    E = V - 1               # 간선 개수

    # tree[현재 노드 번호][0] -> 현재 노드 번호의 왼쪽 자식 노드 번호
    tree = [[0, 0, 0] for _ in range(V + 1)]    # 알파벳, 왼쪽자식, 오른쪽자식

    for i in range(1, V+1):     # 1 ~ V
        data = list(input().split())
        if len(data) >= 2:
            tree[i][0] = data[1]        # 기본적으로 다 알파벳은 있으니까 넣어주고
            if len(data) == 3:          # data에 왼쪽 자식까지 주어진 경우
                tree[i][1] = int(data[2])
            elif len(data) == 4:        # data에 왼쪽, 오른쪽 자식까지 주어진 경우
                tree[i][1] = int(data[2])
                tree[i][2] = int(data[3])

    print(f'#{test}', end=' ')
    in_order(1)
    print()