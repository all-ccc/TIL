import sys
sys.stdin = open('input.txt')

def backtracking(cnt, now):
    global min_cnt
    if cnt >= min_cnt:  # min_cnt 보다 크면 볼 필요도 없다
        return
    if now >= N - 1:    # 목적지 도착!했다면
        if cnt < min_cnt:   # cnt 값 한 번 확인하고
            min_cnt = cnt   # 갱신하고 나서
        return
    else:       # 목적지 도착 못 했다면
        for i in range(1, battery[now] + 1):   # 충전하고 나서(cnt + 1)! 배터리 끝나는 정류장까지 순회(본인 다음부터)
            backtracking(cnt + 1, now + i)

T = int(input())
for test in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    battery = lst[1:]
    min_cnt = 100
    backtracking(-1, 0)     # 첫 정류장에서 충전하는 건 cnt에 포함 안되니까 -1 넣음

    print(f'#{test} {min_cnt}')

