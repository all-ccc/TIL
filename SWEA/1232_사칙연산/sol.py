import sys
# sys.stdin = open('input.txt')

def make_code(k):
    global code
    code.append(tree[k][0])


def post_order(n):
    if n != 0:
        if tree[n][1]:          # 왼쪽 자식의 값이 있으면
            post_order(tree[n][1])
        if tree[n][2]:          # 오른쪽 자식의 값이 있으면
            post_order(tree[n][2])
        make_code(n)
    return code


for test in range(1, 11):
    # N: 정점의 개수
    N = int(input())
    data = [input().split() for _ in range(N)]
    # print('data:', data)
    tree = [[0, 0, 0] for _ in range(N+1)]      # 노드의 값, 왼쪽 자식, 오른쪽 자식
    for i in range(N):
        if len(data[i]) >= 2:
            tree[i+1][0] = data[i][1]     # 일단 기본적으로 노드의 값 저장(정수 혹은 연산자)
            if len(data[i]) == 4:     # 정점이 연산자인 경우(= 자식이 있음)
                tree[i+1][1] = int(data[i][2])    # 왼쪽 자식의 값 저장
                tree[i+1][2] = int(data[i][3])    # 오른쪽 자식의 값 저장
    # print(tree)
    code = []
    cal_result = 0
    result = post_order(1)
    print(result)