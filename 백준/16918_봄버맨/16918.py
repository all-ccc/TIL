from collections import deque
import sys
sys.stdin = open('input.txt')

# 상하좌우
dt_x = [-1, 1, 0, 0]
dt_y = [0, 0, -1, 1]

dq = deque()
# que = deque([start (보통 좌표로 넣음)])

# R : 행, C:열 , N: 시간
R, C, N = map(int, input().split())
arr = [input().split() for _ in range(R)]

# 0초: 폭탄 설치
# 1초: 아무 일 X
# 2초: .에 폭탄 설치
# 3초: 맨첨 설치한 폭탄 터짐
# 맨 첨 설치한 거랑 나중에 설치한 거랑 어떻게 구분함 -> 설치 전 폭탄 위치 어디에 저장 ? 은 덱에 저장
while N != 0:
    # for x in range(R):  # 폭탄 있는 칸
    #     for y in range(C):
    #         if arr[x][y] == 'O':

    N -= 1
    for x in range(R):  # 폭탄 없는 칸에 폭탄 설치
        for y in range(C):
            if arr[x][y] == '.':
                arr[x][y] = 'O'
