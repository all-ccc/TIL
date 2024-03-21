import sys
sys.stdin = open('input.txt')

def make_set(x):
    parent = [i for i in range(x)]  # 노드 번호 수 만큼 parent 리스트 생성
    rank = [0] * x  # 첫 make_set 시행시. 본인을 루트로 하는 노드만 있으므로
    # parent 정보와 rank 정보를 같이 반환
    return parent, rank

def find_set(x):
    # 자기 자신을 부모로 하는 루트 노드를 찾을때까지 탐색
    if parent[x] != x:  # 자기 자신이 대표가 아니면
        parent[x] = find_set(parent[x])     # 다시 찾으러 ㄱㄱ
    return parent[x]


def union(x, y):    # cycle 판별
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 집단의 루트 노드가 서로 다르면 합치는 과정
    if root_x != root_y:
        # 합칠 때, 기준은 rank를 기준으로 작업
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:   # 두 집단의 rank가 동일하다면....
            # 둘 중에 하나 정해서 거기에 붙이고,
            # 해당 집단의 rank를 1 상승 시킨다.
            parent[root_y] = root_x
            rank[root_x] += 1

T = int(input())
for test in range(1, T+1):
    # N: 학생 수, M: 신청서 개수
    N, M = map(int, input().split())    # 5 2
    arr = list(map(int, input().split()))
    parent, rank = make_set(N+1)
    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    # union 작업 후, 평탄화   -> 이거 안 해서 틀린 거임(마지막 인풋값으로 비교해보기)
    for i in range(1, N+1):
        find_set(i)

    p_set = set(parent[1:])
    result = len(p_set)
    # print(parent[1:])
    print(f'#{test} {result}')
