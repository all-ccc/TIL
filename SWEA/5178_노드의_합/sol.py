import sys
# sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    # N: 노드의 개수 / M: 리프 노드의 개수 / L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]  # 리프노드 번호와 자연수가 담긴 data
    tree = [[0] for _ in range(N+1)]     # 왼쪽 자식값, 오른쪽 자식값

    for node, num in data: # 리프 노드 개수만큼 반복문 돌면서 tree의 리프노드 값 저장
        # node = data[i][0]  # data[0]은 리프노드 번호
        # num = data[i][1]   # data[1]은 자연수
        tree[node] = num    # tree에 node를 인덱스로 해서 자연수를 넣어줌
    # print(tree) # 여기까지 하면 리프노드는 저장 끝

    for i in range(N-M, 0, -1):     # 역으로 가면서 자식 노드의 합을 저장해줄 반복문
        left = 2*i
        right = 2*i+1

        if right > N:  # right가 노드의 수보다 크면 (오른쪽 자식은 없다는 거)
            tree[i] = tree[left]
        else:           # 오른쪽 자식까지 있는 경우
            tree[i] = tree[left] + tree[right]
    # print(tree)

    print(f'#{test} {tree[L]}')