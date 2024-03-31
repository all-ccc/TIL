N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()     # 오름차순으로 정렬
max_weight = 0

# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
for i in range(N):  # 0 ~ N-1 까지 순회하면서 로프 몇 개를 쓸 때 최대로 들 수 있는지 알 수 있음
    # 예시 : [15, 20, 30] => 45
    weight = rope[i] * (N-i)    # 현재 들 수 있는 무게
    if weight > max_weight:     # 최대 무게보다 크다면 max_weight 갱신
        max_weight = weight
print(max_weight)