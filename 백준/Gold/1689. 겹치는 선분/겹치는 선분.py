import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
events = []

# 각 구간의 시작과 끝을 이벤트로 저장
for a, b in arr:
    events.append((a, 1))  # 구간의 시작은 +1
    events.append((b, -1)) # 구간의 끝은 -1

# 이벤트들을 정렬
events.sort()

# 현재까지의 겹치는 구간 수와 최대 겹치는 구간 수를 추적
current_overlap = 0
max_overlap = 0
for event in events:
    point, delta = event
    current_overlap += delta  # 이벤트가 발생할 때마다 겹치는 구간의 수를 업데이트
    max_overlap = max(max_overlap, current_overlap)  # 최대 겹치는 구간 수 업데이트

print(max_overlap)
