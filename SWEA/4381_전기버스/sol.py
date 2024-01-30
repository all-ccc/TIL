import sys
# sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    K, N, M = map(int, input().split())
    # K = 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # N = 종점 정류장
    # M = 충전기 설치된 정류장 수
    # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력
    station = list(map(int, input().split())) # 1 3 5 7 9
    now = 0  # 현재 위치
    charge = 0  # 충전 횟수

    while now + K < N:
        if K >= N:  # 충전 없이 한 번에 갈 수 있는 경우
            now = N
            break
        for i in range(len(station)-1, -1, -1): # 최소 충전 횟수를 구하기 위해 역순으로
            if station[i] <= now + K:   # 충전소가 K 내에 있으면
                charge += 1
                now = station[i]
                station = station[i+1:]
                break
            elif i == 0:    # 충전소가 K 내에 없다면
                charge = 0
                now = N   # while문 종료
    print(f'#{test} {charge}')

