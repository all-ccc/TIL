import sys
# sys.stdin = open('input.txt')

def enqueue(n):
    global last
    last += 1       # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # 부모 > 자식 비교를 위해
    p = c // 2      # 부모 번호 계산
    while p >= 1 and h[p] > h[c]:       # 부모가 있는데, 더 크면
        h[p], h[c] = h[c], h[p]         # 교환
        c = p           # 자식이었던 애가 부모가 됨(더 크니까)
        p = c // 2      # 부모였던 애는 자식이 됨 -> 이건 머임


T = int(input())
for test in range(1, T+1):
    N = int(input())
    h = [0] * (N+1)     # 최소힙
    last = 0            # 힙의 마지막 노드 번호
    data = list(map(int, input().split()))
    for i in data:
        enqueue(i)

    result = 0
    while N > 0:
        N //= 2
        result += h[N]
    print(f'#{test} {result}')

