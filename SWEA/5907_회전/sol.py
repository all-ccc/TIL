import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    for i in range(M):
        num = data.pop(0)
        data.append(num)
    result = data[0]
    print(f'#{test} {result}')
