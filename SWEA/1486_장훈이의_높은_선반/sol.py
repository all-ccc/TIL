import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for test in range(1, T+1):
    N, B = map(int, input().split())    # N: 점원 수, B: 선반 높이
    clerk = list(map(int, input().split()))
    min_sum = int(1e9)
    for j in range(1, N+1):
        for k in combinations(clerk, j):
            sum_result = sum(k)
            if sum_result >= B:  # 선반보다 높으면
                min_sum = min(min_sum, sum_result)
    print(f'#{test} {min_sum-B}')