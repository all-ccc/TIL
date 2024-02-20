# import sys
# sys.stdin = open('input.txt')

def solution(k):
    global cnt
    cnt += 1

def preorder(now):  # 조사 시작 노드번호부터 조사를 시작한다.
    # 노드 번호 0은 없음
    if now != 0:
        solution(now)       # 현재 노드 번호에 대해 할 일 수행
        preorder(tree[now][0])
        preorder(tree[now][1])
    return cnt


T = int(input())
for test in range(1, T+1):
    cnt = 0
    # E : 간선의 개수 / N : 루트가 될 노드 번호
    E, N = map(int, input().split())
    V = E + 1
    tree = [[0, 0] for _ in range(V+1)]    # 왼쪽 자식, 오른쪽 자식
    edge = list(map(int, input().split()))
    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if tree[p][0] == 0:     # tree의 왼쪽 자식 정보가 없으면
            tree[p][0] = c      # 넣어줌
        else:                   # 왼쪽 자식 정보가 있으면
            tree[p][1] = c      # 오른쪽에 넣어줌
    result = preorder(N)
    print(f'#{test} {result}')