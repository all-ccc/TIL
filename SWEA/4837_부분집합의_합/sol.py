import sys
# sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    N, K = map(int, input().split())
    # N : 부분 집합 원소 개수
    # K : 원소의 합
    # cnt = 0   # 원소의 합이 K인 부분집합의 개수
    num_list = [i for i in range(1, 13)]
    result_K = []
    cnt = 0

    for i in range(1 << len(num_list)): # 1 << n : 부분 집합의 개수
        temp = []   # i번째 부분집합 넣을 곳
        for j in range(len(num_list)):
            # i번째 부분집합일 때, j번째 요소가 포함되어 있는 부분집합인지 확인하는 코드
            if i & (1 << j):
                temp.append(num_list[j])
        # 여기까지 하면 i번째 부분집합 나옴
        if sum(temp) == K and len(temp) == N: # 부분집합 합이 K가 되면
            cnt += 1

    print(f'#{test} {cnt}')
