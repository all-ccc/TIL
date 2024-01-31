import sys
# sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):   # test case만큼 반복
    grid = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())    # 몇 개의 영역을 칠할지
    purple = 0  # 겹쳐서 보라색이 되는 칸의 수
    for i in range(N):  # 영역 개수만큼 반복
        x1, y1, x2, y2, color = map(int, input().split())
        # [x1, y1]부터 [x2, y2]까지 color로 칠한다
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += color # color의 값을 더해줌

    for row in range(len(grid)): # 2차원 배열이니까 for문 2번 돌림
        for col in grid[row]:
            if col == 3:
                purple += 1

    print(f'#{test} {purple}')