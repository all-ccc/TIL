# import sys
# sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    N = int(input())
    data = [[0] * N for _ in range(N)]
    print(f'#{test}')
    for i in range(N): # 0 1 2 3
        for j in range(i+1):
            if j == 0 or j == i:    # 맨 처음이거나 맨 끝이면
                data[i][j] = 1
            else:
                data[i][j] = data[i-1][j-1] + data[i-1][j]
            print(data[i][j], end= ' ')
        print()