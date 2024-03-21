import sys
sys.stdin = open('input.txt')

# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자.
#   -> 코드로 구현: 전체 간선 정보를 저장 + 가중치로 정렬(정렬이 포인트)

# 2. 방문 처리
#   -> 이때, 싸이클이 발생하면 안된다!
#   -> 싸이클 여부 ?? => union-find 알고리즘이 활용됨

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    # 같은 집합이면 pass
    if x == y:
        return
    # 더 작은 루트노트에 합침
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    edge = []       # 간선 정보들을 모두 저장
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge.append([s, e, w])
    edge.sort(key=lambda x: x[2])
    parents = [i for i in range(V+1)]  #대표자 배열 (자기자신을 바라봄)


    # MST 완성 = 간선의 개수가 V - 1일 때
    cnt = 0  # 선택한 edge의 수
    sum_weight = 0  # MST 가중치의 합
    for s, e, w in edge:
        # 다른 집합이라면
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            sum_weight += w
            if cnt == V:  # MST 구성이 끝나면
                break
    print(f'#{test} {sum_weight}')

