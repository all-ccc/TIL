N = int(input())    # 동아리방 개수
M = int(input())    # 행동 횟수(행동이란 x번 방부터 y번 방 사이의 벽을 무너뜨리는 것)
rooms = [1] * (N+1)
for _ in range(M):
    x, y = map(int, input().split())
    for room in range(x, y):
        rooms[room] = 0     # 부순 방은 0으로

result = rooms.count(1)
print(result-1)